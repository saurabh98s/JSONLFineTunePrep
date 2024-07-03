import os

def ingest_txt(file_path=None):
    # If no file_path is provided, use the project's root directory
    if not file_path:
        # Get the directory of the current script
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # Assuming the file you want to ingest is in the root directory
        # You can modify this path as needed
        file_path = os.path.join("S:\WORK\PROJECTS\gpt-experiments\RawToPrompt", 'main.txt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return content
