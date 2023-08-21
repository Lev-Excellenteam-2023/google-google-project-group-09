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
    words = searching.split()
    if len(words) == 1:
        prefix = words[0]
        locations = trie.search(prefix)
        if locations:
            completions = []
            for file_path, positions in locations.items():
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    for line_number, offset in positions:
                        line = lines[line_number - 1]
                        completion = line.strip()
                        completions.append(completion)
                        if len(completions) >= max_results:
                            return completions
            return completions
    else:
        return []




