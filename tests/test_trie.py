import unittest
from sentence_completion import trie_ds

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = trie_ds.Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple", ("file1.txt", 1, 1))
        self.trie.insert("banana", ("file1.txt", 1, 2))
        self.trie.insert("cherry", ("file1.txt", 2, 1))
        self.trie.insert("apple", ("file2.txt", 1, 1))

        locations_apple = self.trie.search("app")
        locations_banana = self.trie.search("ban")
        locations_grape = self.trie.search("grape")

        self.assertEqual(locations_apple, {
            "file1.txt": [(1, 1), (1, 1)],
            "file2.txt": [(1, 1)]
        })
        self.assertEqual(locations_banana, {
            "file1.txt": [(1, 2)]
        })
        self.assertEqual(locations_grape, {})

    def test_insert_and_search_empty_prefix(self):
        self.trie.insert("apple", ("file1.txt", 1, 1))
        self.trie.insert("banana", ("file1.txt", 1, 2))
        self.trie.insert("cherry", ("file1.txt", 2, 1))
        self.trie.insert("apple", ("file2.txt", 1, 1))

        locations_empty = self.trie.search("")
        self.assertEqual(locations_empty, {})

    def test_search_nonexistent_prefix(self):
        self.trie.insert("apple", ("file1.txt", 1, 1))
        self.trie.insert("banana", ("file1.txt", 1, 2))

        locations_nonexistent = self.trie.search("grape")
        self.assertEqual(locations_nonexistent, {})


if __name__ == '__main__':
    unittest.main()
