class TrieNode:
    def __init__(self):
        self.children = {}
        self.locations = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, location):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        file_path, line_number, offset = location
        if file_path not in node.locations:
            node.locations[file_path] = []
        node.locations[file_path].append((line_number, offset))

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return {}
            node = node.children[char]
        return node.locations
