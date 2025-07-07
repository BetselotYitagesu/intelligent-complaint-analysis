import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Get the absolute path to the vector_store directory
vector_store_path = os.path.abspath("vector_store/")

vector_store = FAISS.load_local(
    vector_store_path,
    embedding_model,
    allow_dangerous_deserialization=True
)


def retrieve_relevant_chunks(query: str, k: int = 5):
    """
    Retrieve top-k relevant chunks from the vector store for a query.

    Args:
        query (str): User question.
        k (int): Number of chunks to retrieve.

    Returns:
        List of docs with page_content and metadata.
    """
    docs = vector_store.similarity_search(
        query,
        k=k
    )
    return docs
