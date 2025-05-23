
# 🔬 Scientific Paper Summarization & Q&A Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-API-green.svg)](https://groq.com)
File Link-https://colab.research.google.com/drive/1C1uQyGKedQGrBBXeIxJhColFsWLovWu9#scrollTo=eCCgZfddxjFp

> 🚀 **AI-powered research assistant that lets scientists ask questions about a corpus of journal articles using RAG (Retrieval-Augmented Generation) with few-shot prompting.**

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [⚙️ Configuration](#️-configuration)

## 🎯 Overview

This project implements a **Scientific Paper Q&A Assistant** that enables researchers to:

- 📚 **Upload multiple PDF papers** to build a searchable corpus
- 🔍 **Ask natural language questions** about the research content
- 🤖 **Get AI-generated answers** with source citations
- 📈 **Evaluate system performance** with comprehensive metrics

### 🔧 Technical Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **LLM** | Llama 3 (via Groq API) | Answer generation |
| **Embeddings** | SentenceTransformers | Semantic search |
| **Vector DB** | FAISS | Fast similarity search |
| **PDF Processing** | PyMuPDF + PyPDF2 | Text extraction |
| **Web Interface** | Streamlit | User interaction |
| **Evaluation** | Custom metrics | Performance assessment |

## ✨ Features

### 🎯 Core Functionality
- **📄 Multi-PDF Ingestion**: Upload and process multiple research papers
- **🧩 Intelligent Chunking**: Semantic text segmentation with overlap
- **🔍 Semantic Search**: Vector-based similarity search across corpus
- **🤖 Few-Shot Learning**: 2+ exemplar pairs guide LLM responses
- **📊 Source Attribution**: Track and display answer sources

### 🌟 Advanced Features
- **🎨 Interactive Web UI**: Streamlit-based interface
- **📈 Performance Metrics**: Comprehensive evaluation framework
- **⚡ Fast Inference**: Groq API for millisecond response times
- **💾 Persistent Storage**: Save and load corpus indices
- **🔄 Real-time Updates**: Dynamic corpus management

## 🏗️ Architecture

graph TD
A[PDF Upload] --> B[Text Extraction]
B --> C[Chunking & Embedding]
C --> D[FAISS Index]
E[User Question] --> F[Similarity Search]
D --> F
F --> G[Context Retrieval]
G --> H[Few-Shot Prompt]
H --> I[Groq API + Llama]
I --> J[Generated Answer]
J --> K[Source Attribution]

text

### 📊 Data Flow

1. **Ingestion Phase**: PDFs → Text Extraction → Chunking → Embeddings → Vector Index
2. **Query Phase**: Question → Similarity Search → Context Retrieval → Prompt Building
3. **Generation Phase**: Few-Shot Prompt → Groq API → Llama Model → Answer + Sources

### ⚡ 5-Minute Setup

1. **Clone the repository**
git clone https://github.com/yourusername/scientific-qa-assistant.git
cd scientific-qa-assistant

text

2. **Install dependencies**
pip install -r requirements.txt

text

3. **Set up API key**
Add to .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

text

4. **Run the application**
streamlit run app.py

text

5. **Open browser**: Navigate to `http://localhost:8501`

## 📦 Installation

### 🐍 Prerequisites
- Python 3.8+
- 4GB+ RAM (for embeddings)
- Internet connection (for Groq API)

### 📋 Dependencies

<details>
<summary>Click to view full requirements.txt</summary>

streamlit>=1.28.0
sentence-transformers>=2.2.2
faiss-cpu>=1.7.4
PyMuPDF>=1.23.0
PyPDF2>=3.0.1
openai>=1.0.0
python-dotenv>=1.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
pandas>=2.0.0
plotly>=5.15.0

text

</details>

or 
Install in Colab
Ref: https://colab.research.google.com/drive/1C1uQyGKedQGrBBXeIxJhColFsWLovWu9#scrollTo=eCCgZfddxjFp
!pip install streamlit sentence-transformers faiss-cpu PyMuPDF openai

Set up tunnel for Streamlit
!npm install -g localtunnel

text

</details>

## ⚙️ Configuration

### 🔑 API Setup

1. **Get Groq API Key**:
   - Visit [Groq Console](https://console.groq.com/)
   - Create account and generate API key
   - Copy the key for configuration

