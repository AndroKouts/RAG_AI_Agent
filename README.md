# RAG AI Agent

A lightweight Retrieval-Augmented Generation (RAG) system that processes PDFs, stores their embeddings, and answers questions grounded in their content. Built with **Inngest**, **Qdrant**, **OpenAI embeddings/LLMs**, **FastAPI**, and a **Streamlit** UI.

---

## 🚀 Features

- 📄 Automated PDF ingestion — chunking, embedding, and indexing  
- 🔄 Event-driven workflows powered by Inngest  
- 🔍 Semantic search using Qdrant  
- 💬 Context-aware answers with GPT-4o-mini  
- 🎨 Clean Streamlit interface for upload & querying  
- 📊 Workflow observability via the Inngest Dev Server  

---

## 🧱 Architecture

```
Streamlit UI → FastAPI Server → Inngest Functions
                                      ↓
                    OpenAI Embeddings + Qdrant Vector DB
```

---

## 📦 Prerequisites

- Python **3.8+**  
- Qdrant server running at **localhost:6333**  
- OpenAI API key  
- Inngest Dev Server running at **localhost:8288**

---

## 🖼️ Screenshots

### Upload PDF
<p align="center">
  <img src="screenshots/pdf_shot.png" width="550" />
</p>

*Upload your PDF documents for extraction and indexing.*

---

### Ask Questions
<p align="center">
  <img src="screenshots/before_asking.png" width="550" />
</p>

*Type any question related to your uploaded documents.*

---

### Get AI Answers
<p align="center">
  <img src="screenshots/after_asking.png" width="550" />
</p>

*Receive grounded, citation-rich answers powered by RAG.*

---





