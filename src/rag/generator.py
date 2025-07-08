from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# New lines (small model)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")


def generate_answer(prompt: str, max_length: int = 256) -> str:
    """
    Generate answer from prompt using flan-t5-base model.

    Args:
        prompt (str): Input prompt containing context + question.
        max_length (int): Maximum length of generated tokens.

    Returns:
        str: Generated answer text.
    """
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, 
                       max_length=512)
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_beams=4,
        early_stopping=True
    )
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer
