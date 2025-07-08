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

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BetselotYitagesu/intelligent-complaint-analysis.git
   cd intelligent-complaint-analysis

   ```

2. **Create and activate a virtual environment:**

python -m venv .venv

# Windows PowerShell

.venv\Scripts\activate

# macOS/Linux

source .venv/bin/activate

3. **Install dependencies:**

pip install -r requirements.txt

Usage
Task 1: Data Exploration & Cleaning

Run the notebook:

    ** jupyter notebook notebooks/01_eda_preprocessing.ipynb **

This notebook covers:

    Data loading and initial analysis

    Filtering relevant product categories

    Text cleaning and saving filtered complaints

# 🧠 Task 2: Text Chunking, Embedding & Vector Store Indexing

This stage is focused on preparing the cleaned complaint narratives for semantic search by transforming them into high-dimensional vector embeddings. These embeddings will later power the Retrieval-Augmented Generation (RAG) pipeline used by the intelligent complaint analysis chatbot.

---

## 🗂️ Workflow Overview

1. **Load Cleaned Dataset**

   - The cleaned and filtered complaint narratives (`filtered_complaints.csv`) from Task 1 are loaded.

2. **Text Chunking**

   - Long complaint narratives are broken into smaller overlapping text chunks using `RecursiveCharacterTextSplitter` from LangChain.
   - This ensures each chunk fits within the token limits of embedding models and improves semantic focus.

3. **Metadata Association**

   - Each chunk is tagged with metadata such as:
     - Product category (e.g., "Credit card", "Money transfers")
     - Complaint ID
   - This metadata enables source tracking during retrieval and improves filtering capabilities.

4. **Embedding Generation**

   - Each chunk is transformed into a semantic vector using the `sentence-transformers/all-MiniLM-L6-v2` model.
   - These vectors capture the meaning of each complaint chunk in a format suitable for similarity search.

5. **Vector Store Indexing**
   - All embeddings are indexed using FAISS (Facebook AI Similarity Search) for fast nearest-neighbor retrieval.
   - Metadata is saved separately for use in the RAG pipeline.

---

## ✅ Task Summary

- 📄 Loaded and processed: `filtered_complaints.csv` with **478,834** records
- 🧩 Generated approximately **1.38 million** text chunks
- 🤖 Used **`all-MiniLM-L6-v2`** model for embedding
- 📦 Stored vectors in a **FAISS index**
- 🏷️ Metadata (product type, complaint ID) saved for traceability and filtering

---

## 📁 Output Files

- `vector_store/faiss_index.index` — Vector index file for semantic search
- `vector_store/metadata.pkl` — Metadata associated with each chunk

---

## 🛠️ Technologies Used

- **LangChain** – Text chunking
- **SentenceTransformers** – Embedding model (`all-MiniLM-L6-v2`)
- **FAISS** – Vector similarity search
- **Pandas & tqdm** – Data processing

---

## 🧩 Next Step

Proceed to **Task 3**: Building the RAG pipeline and evaluating the system's ability to answer real product-related questions from customer complaints.

Task 3: Retrieval-Augmented Generation (RAG) Pipeline & Evaluation
Overview

In Task 3, we built the core logic of the RAG-powered complaint answering system. This involved integrating semantic search over complaint text chunks with a language model to generate concise, insightful answers to user questions.
Key Components

    Retriever: Uses a vector database (FAISS) to perform semantic similarity search on complaint embeddings and retrieve relevant text chunks.

    Prompt Template: Constructs a clear, instructional prompt combining retrieved text excerpts and the user question to guide the LLM.

    Generator: Uses an open-source Hugging Face seq2seq model (google/flan-t5-base) to generate answers locally without requiring API keys.

    Pipeline: Combines retriever, prompt, and generator into a unified interface for querying.

Evaluation

    Developed a set of 5 representative questions to test the system.

    For each question, the pipeline returns an answer and the relevant source excerpts.

    An evaluation table was created (in Markdown format) documenting the question, generated answer, source excerpts, quality score (to be filled manually), and comments.

    This qualitative evaluation highlighted strengths and areas for improvement.

Usage

Example usage snippet:

from src.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline(k=5)
result = rag.answer("Why are users unhappy with Buy Now, Pay Later?")
print(result["answer"])
print(result["sources"][:2]) # Show first two source chunks

Task 4: Interactive Chat Interface
Overview

Task 4 focused on building a user-friendly web interface enabling non-technical users to interact with the RAG pipeline. The interface allows users to type natural language questions and receive answers along with source complaint excerpts for transparency and trust.
Implementation

    Built using Gradio, a Python library for creating simple web UIs quickly.

    The app includes:

        A text input box for user questions.

        A submit button to trigger query processing.

        Output areas showing the AI-generated answer and the source complaint excerpts.

        A clear button to reset the interface.

Running the App

To start the app, run:

python src/ui/app.py

This launches a local web server accessible at http://127.0.0.1:7860.
Screenshots / Demo

Screenshots or a GIF demonstrating the interface are included in the docs/ folder (or embedded in the final report).
User Benefits

    Enables Product Managers, Support, and Compliance teams to quickly query thousands of complaints without technical skills.

    Shows sources to increase answer trustworthiness.

    Reduces time to identify key complaint trends from days to minutes.

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
