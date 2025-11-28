# 📄 Leitor de PDF/Texto com LLM Local (RAG + Ollama)

Este projeto é um **sistema de Retrieval-Augmented Generation (RAG)** que permite:

- Extrair e processar texto de **PDFs** ou texto digitado pelo usuário.
- Recuperar trechos relevantes usando **TF-IDF + FAISS**.
- Gerar respostas ou resumos com **LLM local via Ollama**.
- Interface simples e interativa via **Streamlit**.

---

## 💡 Funcionalidades

1. **Upload de PDF** ou digitação de texto.
2. **RAG**: responde perguntas específicas usando os trechos mais relevantes do texto.
3. **Resumo completo**: gera resumos concisos e diretos de textos longos.
4. **LLM local**: utiliza Ollama para processamento de linguagem natural.
5. Interface **Streamlit** limpa e intuitiva.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.10+**
- **Streamlit** – para interface web
- **PyPDF2** – extração de texto de PDFs
- **Scikit-learn** – TF-IDF
- **FAISS** – indexação vetorial para recuperação de trechos
- **Ollama** – LLM local
- **Subprocess** – integração Python ↔ Ollama
- **Regex** – limpeza e sanitização do texto

---

## ⚡ Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/llm-rag-pdf-ollama.git
cd llm-rag-pdf-ollama
