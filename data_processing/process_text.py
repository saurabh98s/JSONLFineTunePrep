import re

def process_text(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    cleaned_sentences = [sentence for sentence in sentences if len(sentence.split()) > 3]
    return cleaned_sentences
