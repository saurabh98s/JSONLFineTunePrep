from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def filter_sentences_by_topic(sentences, topic, threshold=0.7):
    if not topic:  # If no topic is provided, return all sentences
        return sentences

    topic_embedding = model.encode([topic])
    sentence_embeddings = model.encode(sentences)
    
    similarities = cosine_similarity(topic_embedding, sentence_embeddings)
    
    filtered_sentences = [sentences[i] for i in range(len(sentences)) if similarities[0][i] >= threshold]

    if not filtered_sentences:  # If no sentences are filtered, return all sentences
        return sentences

    print(f"Filtered sentences for topic '{topic}': {filtered_sentences}")  # Debugging line
    return filtered_sentences

def segment_into_chunks(content, delimiter="\n\n"):
    if isinstance(content, list):
        return [chunk.strip() for chunk in content if chunk.strip()]
    elif isinstance(content, str):
        return [chunk.strip() for chunk in content.split(delimiter) if chunk.strip()]
    else:
        raise ValueError("Content must be either a list or a string.")
