# Leitor de PDF/Texto com LLM Local (RAG + Ollama)

<img width="1059" height="585" alt="image" src="https://github.com/user-attachments/assets/05b354e1-8102-43d4-8d9e-00b5118d231c" />

---

### Vídeo demonstrativo
[![Assista ao vídeo](https://img.youtube.com/vi/gjHrPyESfVU/0.jpg)](https://www.youtube.com/watch?v=gjHrPyESfVU)

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

## Fluxo do Projeto

- Usuário fornece texto via PDF ou digitação.
- O texto é quebrado em chunks (tamanho ajustável).
- TF-IDF + FAISS identifica os trechos mais relevantes.
- Prompt é enviado ao LLM via Ollama.
- Resultado é exibido no Streamlit de forma limpa e concisa.

---

## Aplicação Local com Ollama + Streamlit  
Este projeto utiliza modelos LLM executados **localmente**, sem depender de APIs pagas.  
O usuário só precisa ter o **Ollama instalado** e rodando em sua máquina.

### **Instalar o Ollama**  
- Baixe e instale a versão correta para o seu sistema:  
[https://ollama.com/download](https://ollama.com/download)

### 1) Instalação do ambiente, clone o projeto:
```bash
git clone https://github.com/seu-repo/projeto-ollama.git
cd projeto-ollama
```

### 2) Crie o ambiente virtual e instale dependências:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3) Executando o projeto:
```bash
streamlit run app.py
```




























