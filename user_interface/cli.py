import argparse
import re

from trie_processor import load_database_process
from search_complitions import search_completions


# Define your search engine logic here
def clean_text(text):
    # Convert to lowercase, remove punctuation, and replace multiple spaces with a single space
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def search_engine_logic():
    user_input = input("The system is ready. Enter your text:\n")
    return user_input


def main():
    parser = argparse.ArgumentParser(description="Search Engine CLI Google autocomplete project")
    parser.add_argument("-l", "--load", action="store_true", help="Load and analyze text files")
    args = parser.parse_args()
    if args.load:
        print("Loading the file and preparing the system...")
        Trie = load_database_process()
        prefix = search_engine_logic()
        while True:
            if prefix.endswith('#'):
                # break
                prefix = search_engine_logic()

            prefix = clean_text(prefix)
            print("Completing logic and returning offers for:", prefix)
            sentences_list = search_completions(prefix, Trie)
            print("Here are 5 suggestions")
            if sentences_list:
                for sentence in sentences_list:
                    print(sentence)
            print("You can continue typing or type '#' to start over.\n")
            prefix = prefix + " " + input(prefix + " ")


if __name__ == "__main__":
    main()
