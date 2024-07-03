import random
from utils.filter import segment_into_chunks
from prompt_generation.contextual_prompt import ContextualPromptGenerator

def generate_prompt_completion_pairs(prompt,content):
    chunks = segment_into_chunks(content)
    prompt_generator = ContextualPromptGenerator()
    prompts = prompt_generator.generate_prompt(texts=chunks,topic=prompt)
    pairs = list(zip(prompts, chunks))
    return pairs