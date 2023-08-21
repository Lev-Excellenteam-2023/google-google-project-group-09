import argparse
import re

# Define your search engine logic here
def clean_text(text):
    # Convert to lowercase, remove punctuation, and replace multiple spaces with a single space
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Define your search engine logic here
def search_engine_logic():
    # Load and analyze text files
    print("Loading the file and preparing the system...")

    #Rivki's function

    # Get user input
    user_input = input("The system is ready. Enter your text:\n")

    # Perform completion logic and return offers
    print("Completing logic and returning offers for:", clean_text(user_input).split())

    print("Here are 5 suggestions")

    #Avigail's function


def main():
    parser = argparse.ArgumentParser(description="Simple Search Engine CLI")
    parser.add_argument("-l", "--load", action="store_true", help="Load and analyze text files")

    args = parser.parse_args()

    if args.load:
        search_engine_logic()


if __name__ == "__main__":
    main()
