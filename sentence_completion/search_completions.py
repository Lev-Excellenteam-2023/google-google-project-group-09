from sentence_completion import trie_ds


def all_words_found(search_results: list):
    """
    Checks that all the words in the sentence were found in the database.

    Args:
        search_results (list): The locations of each word.

    Returns:
        bool: True if all words found otherwise False.
    """
    return all(locations_dict != {} for locations_dict in search_results)


def search_clause(search_results: list):
    """
    Searches for sentences in which the clause appears.

    Args:
        search_results (list): The locations of each word.

    Returns:
        list: A list of sentences in which the clause appears.
    """
    pass

def find_intersection(dict1, dict2):
    intersection_dictionary = {}

    for filename in dict1:
        if filename in dict2:
            locations_of_word1 = dict1[filename]
            locations_of_word2 = dict2[filename]

            intersection_locations = []

            for location1 in locations_of_word1:
                line1, offset1 = location1

                for location2 in locations_of_word2:
                    line2, offset2 = location2

                    if line1 == line2 and offset1 + 1 == offset2:
                        intersection_locations.append(location2)

            if intersection_locations:
                intersection_dictionary[filename] = intersection_locations

    return intersection_dictionary


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
    completions = []
    words = searching.split()
    if len(words) == 1:
        prefix = words[0]
        locations = trie.search(prefix)
        if locations:
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
        search_results = []
        for word in words:
            locations = trie.search(word)
            search_results.append(locations)
        if all_words_found(search_results):
            completions = search_clause(search_results)
            return completions






