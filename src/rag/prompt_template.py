def build_prompt(context_chunks: list[str], question: str) -> str:
    context = "\n\n".join(context_chunks)
    prompt = (
        f"Use the following customer complaint excerpts to answer question.\n"
        f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    )
    return prompt
