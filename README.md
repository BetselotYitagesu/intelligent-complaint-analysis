# Intelligent Complaint Analysis for Financial Services

## Overview

CrediTrust Financial is a fast-growing digital finance company serving East African markets through a mobile-first platform. Handling thousands of customer complaints monthly across multiple product categories, they face challenges in extracting actionable insights from unstructured complaint narratives.

This project delivers an **AI-powered Retrieval-Augmented Generation (RAG) chatbot** that transforms raw customer complaints into concise, evidence-backed insights. It enables product managers, support, and compliance teams to quickly identify major issues, speeding up decision-making from days to minutes.

---

## Features

- **Semantic Search with Vector Databases:** Uses advanced embedding models and vector similarity search (via FAISS or ChromaDB) to retrieve the most relevant complaint narratives.
- **Natural Language Querying:** Allows non-technical users to ask questions in plain English and receive grounded, summarized answers.
- **Multi-product Analysis:** Supports querying and comparing across five key financial products:
  - Credit Cards
  - Personal Loans
  - Buy Now, Pay Later (BNPL)
  - Savings Accounts
  - Money Transfers
- **Interactive Chat Interface:** Built with Gradio/Streamlit for ease of use by internal stakeholders.
- **Modular Codebase:** Clear separation of data preprocessing, embedding, retrieval, generation, and UI components.

---

## Project Structure

intelligent-complaint-analysis/
├── data/
│ └── filtered_complaints.csv # Cleaned dataset for embedding & retrieval
├── notebooks/
│ ├── 01_eda_preprocessing.ipynb # Task 1: Data exploration & cleaning
│ ├── 02_chunking_embedding_indexing.ipynb # Task 2: Text chunking & vector store
│ ├── 03_rag_pipeline_evaluation.ipynb # Task 3: Retrieval + generation + evaluation
│ └── 04_chat_interface.ipynb # Task 4: Interactive UI
├── src/
│ ├── preprocessing/ # Scripts for data cleaning and preprocessing
│ ├── embedding/ # Embedding & vector store logic
│ ├── rag/ # RAG pipeline code (retriever + generator)
│ └── ui/ # Web app code using Gradio or Streamlit
├── vector_store/ # Persisted vector index files
├── requirements.txt # Python dependencies
├── README.md # This file
└── interim_report.md # Progress report for Task 1 & 2

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BetselotYitagesu/intelligent-complaint-analysis.git
   cd intelligent-complaint-analysis

   ```

2. Create and activate a virtual environment:

python -m venv .venv

# Windows PowerShell

.venv\Scripts\activate

# macOS/Linux

source .venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

Usage
Task 1: Data Exploration & Cleaning

Run the notebook:

    ** jupyter notebook notebooks/01_eda_preprocessing.ipynb **

This notebook covers:

    Data loading and initial analysis

    Filtering relevant product categories

    Text cleaning and saving filtered complaints

Task 2: Text Chunking, Embedding & Vector Store Creation

Process cleaned complaints into chunks, generate embeddings, and create a vector index for retrieval.
Task 3: Build RAG Pipeline & Evaluate

Implement the retriever and LLM generator pipeline, then perform qualitative evaluation with test questions.
Task 4: Interactive Chat Interface

Launch the chatbot UI for querying customer complaints in natural language.
Technologies & Tools

    Python 3.8+

    Pandas, Matplotlib, Seaborn — Data analysis & visualization

    FAISS / ChromaDB — Vector similarity search

    SentenceTransformers (e.g., all-MiniLM-L6-v2) — Text embeddings

    LangChain or HuggingFace — RAG pipeline orchestration

    Gradio / Streamlit — Interactive UI development

    Git & GitHub — Version control and collaboration

Learning Outcomes

    Master combining vector search and language models for question answering

    Handle noisy, unstructured complaint data at scale

    Build and manage vector stores with metadata

    Perform prompt engineering for effective LLM responses

    Develop user-friendly AI tools for business stakeholders

Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.
License

This project is for educational purposes. Please contact the author for commercial use.
