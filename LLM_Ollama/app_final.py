import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np
import subprocess
import re
from typing import List

# ---------------------------------------------------------
# CONFIGURAÇÃO DO OLLAMA
# ---------------------------------------------------------
OLLAMA_DEFAULT = r"C:\Users\Meu Computador\AppData\Local\Programs\Ollama\ollama.exe"
DEFAULT_MODEL = "llama3.2:latest"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 5

# ---------------------------------------------------------
# FUNÇÕES ÚTEIS
# ---------------------------------------------------------
def read_pdf(file) -> str:
    """Extrai texto de PDF"""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def chunk_text(text: str, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP) -> List[str]:
    """Divide texto em chunks"""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - chunk_overlap
    return chunks

def build_tfidf_index(chunks: List[str]):
    """Cria vetor TF-IDF e índice FAISS"""
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(chunks)
    arr = X.toarray().astype(np.float32)
    dim = arr.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(arr)
    return vectorizer, index, arr

def query_top_k(query: str, vectorizer: TfidfVectorizer, index: faiss.IndexFlatL2, chunks: List[str], k=TOP_K):
    """Recupera top-k chunks relevantes"""
    qv = vectorizer.transform([query]).toarray().astype(np.float32)
    D, I = index.search(qv, k)
    return [chunks[i] for i in I[0].tolist()]

def perguntar_ollama(prompt: str, modelo: str, ollama_cmd: str):
    """Envia prompt para Ollama via subprocess com UTF-8"""
    try:
        result = subprocess.run(
            [ollama_cmd, "run", modelo],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Erro: {str(e)}"

def sanitize(text: str) -> str:
    """Remove caracteres estranhos mantendo acentuação"""
    text = re.sub(r'[\u2800-\u28FF]+', '', text)
    return text.encode('utf-8', errors='ignore').decode('utf-8').strip()

# ---------------------------------------------------------
# STREAMLIT UI
# ---------------------------------------------------------
st.set_page_config(page_title="RAG PDF/Texto + Ollama", layout="wide")
st.title("📄 Leitor de PDF ou Texto com LLM (Ollama)")

# Barra lateral
st.sidebar.header("Sobre o projeto")
st.sidebar.markdown("""
Este projeto demonstra um sistema de **RAG (Retrieval-Augmented Generation)** local usando:

- **Python + Streamlit** para interface minimalista.
- **Ollama LLM** rodando localmente.
- **TF-IDF + FAISS** para recuperar trechos relevantes.
- Suporte a **upload de PDF ou inserção de texto**.
- **Resumo completo de textos longos** usando chunking grande.

Fluxo técnico resumido:
1. Receber texto via upload ou campo de texto.
2. Escolher operação: pergunta específica ou resumo completo.
3. Se pergunta: RAG com top-k chunks.
4. Se resumo: enviar texto inteiro (ou grandes blocos) para LLM.
5. Exibir resposta limpa e direta.

**Contatos:**  
[LinkedIn](https://www.linkedin.com/in/jeduardosleite/) | [GitHub](https://github.com/jeduardosleite)
""")

# Configurações
st.sidebar.header("Configurações")
modelo = st.sidebar.text_input("Modelo Ollama", DEFAULT_MODEL)
ollama_cmd = st.sidebar.text_input("Caminho do Ollama", OLLAMA_DEFAULT)
top_k = st.sidebar.number_input("Número de chunks a recuperar (k)", min_value=1, max_value=20, value=TOP_K)

# Fonte do texto
modo = st.radio("Escolha a fonte do texto:", ["Upload de PDF", "Escrever texto"])
texto = ""
if modo == "Upload de PDF":
    arquivo_pdf = st.file_uploader("Envie o PDF", type=["pdf"])
    if arquivo_pdf:
        with st.spinner("Extraindo texto do PDF..."):
            texto = read_pdf(arquivo_pdf)
            st.success(f"Texto extraído: {len(texto)} caracteres")
elif modo == "Escrever texto":
    texto = st.text_area("Digite seu texto aqui:", height=300)

# Operação: Pergunta ou Resumo
operacao = st.radio("Escolha a operação:", ["Pergunta específica", "Resumo completo"])

# Pergunta
pergunta = ""
if operacao == "Pergunta específica":
    pergunta = st.text_input("Faça uma pergunta sobre o texto ou PDF")

if texto and ((operacao == "Resumo completo") or (operacao == "Pergunta específica" and pergunta)):
    with st.spinner("Processando..."):
        if operacao == "Pergunta específica":
            # RAG
            chunks = chunk_text(texto)
            vectorizer, index, _ = build_tfidf_index(chunks)
            top_chunks = query_top_k(pergunta, vectorizer, index, chunks, k=top_k)
            contexto_prompt = "\n".join(top_chunks)
            prompt_text = f"""
Você é um assistente que responde somente com base no texto fornecido.
Não invente nomes, eventos ou detalhes. Seja direto e objetivo.

TEXTO DISPONÍVEL:
-----------------
{contexto_prompt}
-----------------

PERGUNTA:
{pergunta}

RESPOSTA FINAL:
"""
        else:
            # Resumo completo
            prompt_text = f"""
Você é um assistente que faz **resumo de texto completo**.
Resuma o texto abaixo em parágrafo(s) claros e concisos, mantendo a informação essencial.
Não invente detalhes.

TEXTO:
-----------------
{texto}
-----------------

RESUMO FINAL:
"""
        resposta = perguntar_ollama(prompt_text, modelo, ollama_cmd)
        st.subheader("Resultado:")
        st.write(sanitize(resposta))
