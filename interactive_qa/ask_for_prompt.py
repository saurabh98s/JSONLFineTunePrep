from prompt_generation.contextual_prompt import ContextualPromptGenerator

def ask_for_prompt(topic,cleaned_sentences):
    if topic.strip() == '':
        # Using the AI-driven contextual prompt generator to infer a topic
        generator = ContextualPromptGenerator()
        topic_summary = generator.generate_prompt(" ".join(cleaned_sentences))
        
        # Given that the output is a summary, we can frame it as a question
        topic_question = f"What can you tell me about {topic_summary}?"
        print(topic_question)
        print(f"Suggested Topic: {topic_question}")
        return topic_question

    return topic
