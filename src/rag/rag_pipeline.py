from typing import Dict, Any, List
from src.rag.retriever import ComplaintRetriever
from src.rag.prompt_template import build_prompt
from src.rag.generator import generate_answer


class RAGPipeline:
    def __init__(self, k: int = 5, debug: bool = False) -> None:
        self.retriever = ComplaintRetriever()
        self.k = k
        self.debug = debug

    def answer(self, question: str) -> Dict[str, Any]:
        retrieved_chunks: List[Dict[str, Any]] = self.retriever.retrieve(
            question, k=self.k
        )
        print("Retrieved chunks:", retrieved_chunks)
        print("First item keys:", retrieved_chunks[0].keys())

        chunk_texts = [item["content"] for item in retrieved_chunks]  # ✅

        if self.debug:
            print("Sample retrieved chunk:\n", retrieved_chunks[0])

        prompt = build_prompt(chunk_texts, question)
        response = generate_answer(prompt)

        return {
            "question": question,
            "answer": response,
            "sources": chunk_texts,
        }
