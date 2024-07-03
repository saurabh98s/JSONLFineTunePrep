from transformers import BartForConditionalGeneration, BartTokenizer
from transformers import T5ForConditionalGeneration, T5Tokenizer

class ContextualPromptGenerator:
    def __init__(self, use_t5=False):
        if use_t5:
            self.model_name = "t5-base"
            self.model = T5ForConditionalGeneration.from_pretrained(self.model_name)
            self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
            self.max_length = 512
        else:
            self.model_name = "facebook/bart-large-cnn"
            self.model = BartForConditionalGeneration.from_pretrained(self.model_name)
            self.tokenizer = BartTokenizer.from_pretrained(self.model_name)
            self.max_length = 1024

    def generate_prompt(self, texts, topic=None):
        if topic:
            texts = [f"{topic}: {text}" for text in texts]

        inputs = self.tokenizer(texts, padding=True, truncation=True, max_length=self.max_length, return_tensors="pt")

        if self.model_name == "t5-base":
            summary_ids = self.model.generate(inputs["input_ids"], num_beams=4, num_return_sequences=1, early_stopping=True)
        else:
            summary_ids = self.model.generate(inputs["input_ids"], num_beams=4, num_return_sequences=1, early_stopping=True)

        prompts = [self.tokenizer.decode(g, skip_special_tokens=True) for g in summary_ids]

        prompt_completion_pairs = []
        for idx, prompt in enumerate(prompts):
            pair = {"prompt": prompt, "completion": texts[idx]}
            prompt_completion_pairs.append(pair)

        return prompt_completion_pairs
