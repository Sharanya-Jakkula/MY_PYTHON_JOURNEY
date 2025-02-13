import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import re

def list_files(target_directory):
    file_paths = []
    for root, _, files in os.walk(target_directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def count_word_in_text(file_path, word):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        return content.lower().split().count(word.lower())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def count_word_in_excel(file_path, word):
    try:
        df = pd.read_excel(file_path)
        count = 0
        for column in df.columns:
            count += df[column].astype(str).str.lower().str.count(re.escape(word.lower())).sum()
        return count
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def process_file(file_path, word):
    if file_path.endswith('.txt'):
        return file_path, count_word_in_text(file_path, word)
    elif file_path.endswith('.xlsx'):
        return file_path, count_word_in_excel(file_path, word)
    else:
        return file_path, 0

def main(target_directory, word):
    file_paths = list_files(target_directory)
    filtered_paths = [path for path in file_paths if path.endswith('.txt') or path.endswith('.xlsx')]
    
    results = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, path, word) for path in filtered_paths]
        for future in futures:
            results.append(future.result())
    
    for file_path, count in results:
        print(f"{file_path}: {count}")

if __name__ == "__main__":
    target_directory = input("Enter the path: ")
    word = input("Enter the word : ")
    main(target_directory, word)
