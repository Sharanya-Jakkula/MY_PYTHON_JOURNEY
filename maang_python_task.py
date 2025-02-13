import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

def list_files(path):
    file_paths = []
    for root, _, files in os.walk(path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def file_type(file):
    ext = file.split('.')[-1]
    if ext == 'txt':
        return "txt"
    elif ext == 'xlsx':
        return "xlsx"
    elif ext == 'csv':
        return "csv"
    else:
        return 'other'

def read_file(path, word):
    count = 0
    with open(path, "r") as file:
        for line in file.readlines():
            count += line.lower().split().count(word.lower())
    return count

def read_csv(path, word):
    word = word.lower()
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower()
    count = df.applymap(lambda x: str(x).count(word)).sum().sum()
    return count

def read_xlsx(path, word):
    data = pd.read_excel(path)
    df = pd.DataFrame(data)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower()
    count = df.applymap(lambda x: str(x).count(word)).sum().sum()
    return count

def read_mode(file_paths, word):
    total_count = 0
    with ThreadPoolExecutor() as executor:
        future_to_path = {executor.submit(read_file_type, path, word): path for path in file_paths}
        for future in as_completed(future_to_path):
            total_count += future.result()
    return total_count

def read_file_type(path, word):
    ext = file_type(path)
    if ext == 'txt':
        return read_file(path, word)
    elif ext == 'csv':
        return read_csv(path, word)
    elif ext == 'xlsx':
        return read_xlsx(path, word)
    else:
        return 0

def assemble(path, word):
    file_paths = list_files(path)
    count = read_mode(file_paths, word)
    print("\nFiles in the given target directory are  : \n")
    for i in file_paths:
        print(i)
    print(f"\nThe Count of the word '{word}' is {count} \n")

if __name__ == "__main__":
    path = input("Enter the path : ")
    word = input("Enter the word to find the word count : ")
    assemble(path, word)
