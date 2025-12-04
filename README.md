# RAG AI Agent

A Retrieval-Augmented Generation application that processes PDFs using Inngest workflows and answers questions about their content. Built with Qdrant vector database, OpenAI embeddings/LLM, FastAPI backend, and Streamlit UI.

## Features

- 📄 PDF processing with automatic chunking and indexing
- 🔄 Event-driven architecture with Inngest workflows
- 🔍 Semantic search using Qdrant vector database
- 💬 AI-powered answers with GPT-4o-mini
- 🎨 Simple Streamlit UI for upload and querying
- 📊 Observable workflows via Inngest Dev Server

## Architecture

```
Streamlit UI → FastAPI Server → Inngest Functions
                                      ↓
                    OpenAI Embeddings + Qdrant Vector DB
```

## Prerequisites

- Python 3.8+
- Qdrant Server (running on `localhost:6333`)
- OpenAI API Key
- Inngest Dev Server (running on `localhost:8288`)

## Screenshots

### Upload PDF
![PDF Upload Interface](screenshots/upload_pdf.png)
*Upload your PDF documents for processing and indexing*

### Ask Questions
![Query Interface - Before](screenshots/query_before.png)
*Enter your question about the ingested documents*

### Get AI Answers
![Query Interface - After](screenshots/query_after.png)
*Receive context-based answers with source citations*

