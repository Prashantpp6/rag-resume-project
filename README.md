# 🚀 Resume Chatbot using RAG

An AI-powered chatbot that can intelligently answer questions about a resume using **Retrieval-Augmented Generation (RAG)**.

---

## 📌 Overview

This project allows users to upload a resume (PDF) and ask questions about it.
The system retrieves relevant information from the document and generates accurate answers using an LLM.

---

## ⚡ Features

* 📄 Upload PDF resume
* 🔍 Semantic search using FAISS
* 🤖 Context-aware responses (no hallucination)
* ⚡ Fast inference using Groq LLM
* 💬 Interactive UI built with Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* FAISS (Vector Database)
* HuggingFace Embeddings
* Groq (LLaMA 3)

---

## 🧠 How It Works

1. Resume is uploaded and converted into text
2. Text is split into smaller chunks
3. Embeddings are created using HuggingFace
4. Stored in FAISS vector database
5. User query is matched with relevant chunks
6. LLM generates answer using retrieved context

---

## 📂 Project Structure

```
rag-resume-project/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/Prashantpp6/rag-resume-project.git
cd rag-resume-project
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
python -m streamlit run app.py
```

---

## 🎯 Use Case

* Resume analysis
* Interview preparation
* Personal AI assistant for CV queries

---

## 👨‍💻 Author

**Prashant Singh Parmar**
🔗 LinkedIn: https://www.linkedin.com/in/prashant-singh-parmar/
💻 GitHub: https://github.com/Prashantpp6

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
