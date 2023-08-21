from sentence_completion import trie_ds


def search_completions(searching: str, trie: trie_ds.Trie, max_results=5):
    """
    Searches for sentence completions by splitting the sentence into words and finding completions for each word.

    Args:
        searching (str): The input sentence to search for completions.
        trie (Trie): The Trie data structure containing the word locations.
        max_results (int): The maximum number of results to return per word completion.

    Returns:
        list: A list of sentences where each word in the input sentence exists.
    """
    return []




