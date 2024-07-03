from utils.filter import filter_sentences_by_topic
from data_ingestion.ingest_text import ingest_txt
from data_processing.process_text import process_text
from interactive_qa.ask_for_prompt import ask_for_prompt
from prompt_completion.create_pair import generate_prompt_completion_pairs
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    file_path = input("Enter the path of the .txt file: ")
    topic = input("Do you want to specify a specific topic? If not, press Enter: ")

    raw_content = ingest_txt(file_path)
    cleaned_sentences = process_text(raw_content)
    print(cleaned_sentences)
    
    # If a topic is specified, filter the sentences
    if topic:
        cleaned_sentences = filter_sentences_by_topic(cleaned_sentences, topic)

    # Generate prompt
    prompt = ask_for_prompt(topic,cleaned_sentences)  # or generate using ContextualPromptGenerator
    
    if not prompt:
        print("No suitable prompt could be generated.")
        return

    # Generate completion
    pair = generate_prompt_completion_pairs(prompt, cleaned_sentences)  
    print("\nGenerated Prompt-Completion Pair:")
    print(pair)

if __name__ == "__main__":
    main()
