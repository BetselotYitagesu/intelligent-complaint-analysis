from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vector_store = FAISS.load_local(
    "vector_store/",
    embedding_model
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
