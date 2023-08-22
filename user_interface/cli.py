import argparse
import re

import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))

parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from sentence_completion import trie_processor
from sentence_completion import search_complitions


def clean_text(text):
    """
       Clean the input text by converting to lowercase, removing punctuation, and extra spaces.

       Parameters:
       - text (str): The input text to be cleaned.

       Returns:
       - str: The cleaned text.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def search_engine_logic():
    """
       Get user input and return it.

       Returns:
       - str: The user's input text.
       """
    user_input = input("The system is ready. Enter your text:\n")
    return user_input


def main():
    parser = argparse.ArgumentParser(description="Search Engine CLI Google autocomplete project")
    parser.add_argument("-l", "--load", action="store_true", help="Load and analyze text files")
    parser.add_argument("-e", "--end", action="store_true", help="End the program")

    args = parser.parse_args()
    if args.end:
        print("Exiting the program.")
        return

    if args.load:
        print("Loading the file and preparing the system...")
        Trie = trie_processor.load_database_process()
        prefix = search_engine_logic()
        while True:
            if prefix.endswith('#'):
                # break
                prefix = search_engine_logic()

            prefix = clean_text(prefix)
            print("Completing logic and returning offers for:", prefix)
            sentences_list = search_complitions.search_completions_(prefix, Trie)
            print("Here are 5 suggestions")
            if sentences_list:
                for sentence in sentences_list:
                    print(sentence)
            print("You can continue typing or type '#' to start over.\n")
            prefix = prefix + " " + input(prefix + " ")


if __name__ == "__main__":
    main()
