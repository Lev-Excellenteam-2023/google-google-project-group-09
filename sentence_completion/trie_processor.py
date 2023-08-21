import re
import os

from sentence_completion import trie_ds


def process_text_file(file_path: str, trie: trie_ds.Trie):
    """
    Processes a text file, extracts words, and inserts them into the Trie along with their locations.

    Args:
        file_path (str): The path to the text file.
        trie (Trie): The Trie data structure to insert the words into.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            words = re.findall(r'\w+', line.lower())
            for offset, word in enumerate(words, start=1):
                trie.insert(word, (file_path, line_number, offset))


def process_folder(folder_path: str, trie: trie_ds.Trie):
    """
    Processes all text files within a folder and its subfolders.

    Args:
        folder_path (str): The path to the folder containing text files.
        trie (Trie): The Trie data structure to insert the words into.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                process_text_file(file_path, trie)