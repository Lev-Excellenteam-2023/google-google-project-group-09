class TrieNode:
    """
    Represents a node in the Trie data structure.

    Attributes:
        children (dict): A dictionary storing child nodes based on characters.
        locations (dict): A dictionary storing word locations within files.
            Key: File path
            Value: List of tuples (line number, offset) where the word occurs
    """

    def __init__(self):
        self.children = {}
        self.locations = {}


class Trie:
    """
    Represents a Trie data structure used for efficient word storage and retrieval.

    Attributes:
        root (TrieNode): The root node of the Trie.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, location:tuple):
        """
        Inserts a word along with its location into the Trie.

        Args:
            word (str): The word to be inserted.
            location (tuple): A tuple representing the location of the word.
                Format: (file_path, line_number, offset)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        file_path, line_number, offset = location
        if file_path not in node.locations:
            node.locations[file_path] = []
        node.locations[file_path].append((line_number, offset))

    def search(self, prefix:str):
        """
        Searches for all word locations that match the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            dict: A dictionary containing word locations based on file paths.
                Key: File path
                Value: List of tuples (line number, offset) where the words matching the prefix occur.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return {}
            node = node.children[char]
        return node.locations
