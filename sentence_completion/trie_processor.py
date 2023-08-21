import re
import os


def process_text_file(file_path, trie):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            words = re.findall(r'\w+', line.lower())
            for offset, word in enumerate(words, start=1):
                trie.insert(word, (file_path, line_number, offset))


def process_folder(folder_path, trie):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                process_text_file(file_path, trie)


