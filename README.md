# Intelligent Complaint Analysis for Financial Services

## Overview

CrediTrust Financial is a fast-growing digital finance company serving East African markets through a mobile-first platform. The company handles thousands of customer complaints monthly across multiple product categories, creating challenges in extracting actionable insights from unstructured complaint narratives.  

This project delivers a **complete AI-powered Retrieval-Augmented Generation (RAG) pipeline** that transforms raw customer complaints into concise, evidence-backed insights. It enables product managers, support, and compliance teams to identify key issues quickly, reducing analysis time from days to minutes.

---

## Features

- **Semantic Search with Vector Databases:** Uses advanced embedding models and vector similarity search (FAISS) to retrieve the most relevant complaint narratives.  
- **Natural Language Querying:** Non-technical users can ask questions in plain English and receive grounded, summarized answers.  
- **Multi-product Coverage:** Supports querying across five key financial products:
  - Credit Cards
  - Personal Loans
  - Buy Now, Pay Later (BNPL)
  - Savings Accounts
  - Money Transfers  
- **Interactive Chat Interface:** Built with Gradio for an easy-to-use web interface.  
- **Modular Codebase:** Clear separation of preprocessing, embedding, retrieval, generation, and UI components for maintainability.  

---

## Project Structure


intelligent-complaint-analysis/
├── data/
│ └── filtered_complaints.csv # Cleaned dataset for embedding & retrieval
├── notebooks/
│ ├── 01_eda_preprocessing.ipynb # Task 1: Data exploration & cleaning
│ ├── 02_chunking_embedding_indexing.ipynb # Task 2: Text chunking & vector store
│ ├── 03_rag_pipeline_evaluation.ipynb # Task 3: RAG pipeline & evaluation
│ └── 04_chat_interface.ipynb # Task 4: Interactive chat UI
├── src/
│ ├── preprocessing/ # Data cleaning scripts
│ ├── embedding/ # Embedding and vector store logic
│ ├── rag/ # RAG pipeline modules (retriever + generator)
│ └── ui/ # Gradio chat interface code
├── vector_store/ # Persisted vector indices and metadata
├── requirements.txt # Python dependencies
├── README.md # This file
└── interim_report.md # Progress report for Tasks 1 & 2



---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/BetselotYitagesu/intelligent-complaint-analysis.git
cd intelligent-complaint-analysis

2. Create and activate a virtual environment:

python -m venv .venv

# Windows PowerShell
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

Usage

Task 1: Data Exploration & Preprocessing

Run the notebook:
    
    jupyter notebook notebooks/01_eda_preprocessing.ipynb

This covers:

Data loading and initial analysis

Filtering for relevant product categories

Text cleaning (lowercasing, removing URLs/special characters, collapsing whitespace)

Saving filtered complaints for embedding

Task 2: Text Chunking, Embedding & Vector Indexing

Chunking: Long complaints split into overlapping chunks (500 tokens with 50-token overlap).

Metadata: Attach Complaint ID and Product category for traceability.

Embeddings: Use all-MiniLM-L6-v2 model.

Indexing: Store chunks in FAISS for fast retrieval.

Output Files:

vector_store/faiss_index.index — FAISS vector index

vector_store/metadata.pkl — Metadata for each chunk

Task 3: RAG Pipeline & Evaluation

Retriever: FAISS-based semantic search.

Prompt Template: Formats retrieved text + user query.

Generator: google/flan-t5-base generates answers.

Pipeline: Unified interface for querying complaints in natural language.

Example Usage:

from src.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline(k=5)
result = rag.answer("Why are users unhappy with Buy Now, Pay Later?")
print(result["answer"])
print(result["sources"][:2])


**Evaluation Table Example:**

| Question                              | Answer                               | Sources (truncated)                      | Score | Comments               |
|--------------------------------------|-------------------------------------|----------------------------------------|-------|------------------------|
| Why are users unhappy with BNPL?      | They are unresponsive               | [Credit card complaint text…]           | 3     | Lack of context        |
| Are there complaints about credit card billing? | yes                         | ['[Credit card] subject deceptive billing…'] | 4     | Short but relevant     |
| What issues do customers report with savings accounts? | account access & customer service | ['[Savings account] formal complaint…'] | 4.5   | Good                   |
| Top complaints about money transfers? | scams                               | ['[Money transfers] transfers difficult…'] | 4     | Relevant but brief     |
| Problems with loan repayment?         | no                                  | ['[Personal loan] borrowed 100000…']   | 3.5   | Lacks context          |


Task 4: Interactive Chat Interface

Built with Gradio: Real-time question answering with source grounding.

Features: Input box, submit button, output area, Clear button.

Run the app:
    python src/ui/app.py
Access at: http://127.0.0.1:7860

Output & Benefits

Fast, interactive querying of thousands of complaints

AI-generated insights with source references

Reduces analysis time from days to minutes

Supports Product, Support, and Compliance teams

Technologies Used

Python 3.8+

Pandas, Matplotlib, Seaborn

SentenceTransformers (all-MiniLM-L6-v2)

FAISS

LangChain / HuggingFace

Gradio / Streamlit

Git & GitHub

Learning Outcomes

Preprocessing large-scale complaint data

Chunking text and generating embeddings

Building and evaluating a RAG pipeline

Developing a user-friendly AI chat interface

Understanding prompt engineering and vector-based search
