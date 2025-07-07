from src.rag.retriever import retrieve_relevant_chunks
from src.rag.prompt_template import RAG_PROMPT_TEMPLATE
from src.rag.generator import generate_answer


def rag_pipeline(query: str, k: int = 5):
    """
    Full RAG pipeline: retrieve, prompt, generate.

    Args:
        query (str): User question.
        k (int): Number of chunks to retrieve.

    Returns:
        answer (str), docs (list)
    """
    docs = retrieve_relevant_chunks(
        query,
        k=k
    )
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = RAG_PROMPT_TEMPLATE.format(
        context=context,
        question=query
    )
    answer = generate_answer(prompt)
    return answer, docs
