"""
Rag pipeline generator
"""
from transformers.pipelines import pipeline

# Initialize text generation pipeline with appropriate device setting
qa_pipeline = pipeline(
    "text-generation",
    model="tiiuae/falcon-7b-instruct",
    device=0
)


def generate_answer(prompt: str, max_tokens: int = 200):
    """
    Generate answer from LLM based on the prompt.

    Args:
        prompt (str): Prompt text including context & question.
        max_tokens (int): Max tokens to generate.

    Returns:
        Generated answer (str).
    """
    outputs = qa_pipeline(
        prompt,
        max_new_tokens=max_tokens,
        do_sample=True
    )
    generated_text = outputs[0]["generated_text"]
    return generated_text
