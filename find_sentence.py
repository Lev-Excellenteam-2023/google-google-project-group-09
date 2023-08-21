
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

dict1 = {
    'file1.txt': [(1, 2), (1, 3), (2, 5), (2, 6), (3, 1)],
    'file2.txt': [(1, 1), (1, 3), (2, 5), (3, 6), (2, 6)],
    'file3.txt': [(1, 1), (1, 3), (2, 5), (3, 6), (2, 6)]
}

dict2 = {
    'file1.txt': [(1, 4), (2, 5), (2, 6), (3, 2)],
    'file2.txt': [(1, 2), (2, 6), (2, 7)]
}

intersection_result = find_intersection(dict1, dict2)
print(intersection_result)











