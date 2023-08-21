import unittest
from unittest.mock import Mock
from sentence_completion import trie_ds, search_completions


class TestSearchCompletions(unittest.TestCase):

    def test_single_word_completion(self):
        # Prepare mock Trie instance with search results
        mock_trie = Mock()
        mock_trie.search.return_value = {
            r'rfc7541.txt': [(2492, 11)],
            r'Tasks.txt': [(12217, 11)]
        }

        # Test the search_completions function
        completions = search_completions.search_completions('examp', mock_trie)

        # Assertions
        expected_completions = ['7474 7073 3a2f 2f77 7777 2e65 7861 6d70 | ttps://www.examp',
                                'extended resource names have the form example.com/foo where examp']
        self.assertEqual(completions, expected_completions)


if __name__ == '__main__':
    unittest.main()
