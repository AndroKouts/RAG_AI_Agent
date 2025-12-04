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
