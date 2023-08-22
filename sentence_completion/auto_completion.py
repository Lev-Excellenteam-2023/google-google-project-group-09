class Autocomplete:
    def _init_(self,status,input_word,index,location):
        self.__status = status
        self.__input_word = input_word
        self.__index= index
        self.__dict_loc=location
        self.__score= self.get_score(self)

    def get_score(self):
        if self.__status == 'not_changed':
            return len(self.__input_word) * 2
        elif self.__status == 'add_one' or self.__status == 'delete_one':
            if self.__index > 3:
                return (len(self.__input_word) * 2) - 2
            else:
                return (len(self.__input_word) * 2) - (10 - self.__index * 2)
        elif self.__status == 'changed':
            if self.__index > 4:
                return (len(self.__input_word) * 2) - 1
            else:
                return (len(self.__input_word) * 2) - (5 - self.__index)

    def find_words_changed(self, char):
        '''
        :param char: word with mistake
        :return: list of all possible words that appear in the dataset, with one change
        the list is in format [word,offset, dictionary]
        '''
        i = 0
        orig = ''
        list_words = []
        dict = {}
        while (i != len(char)):
            orig = char[i]
            for j in keyboard_layout[char[i]]:
                char[i] = j
                dict = search(char)
                if (dict == {}):
                    continue
                else:
                    # adds [word,offset,dictionray
                    list_words.append([char, i, dict])
            # there can only be one mistake so therefore put back the original letter
            char[i] = orig
        return list_words

    def find_words_add(self, char):
        '''
       :param char: word with mistake
       :return: list of all possible words that appear in the dataset, with extra letter added
       the list is in format [word,offset, dictionary]
       '''
        i = 0
        abc = []
        orig = ''
        list_words = []
        dict = {}
        word = ''
        while (i != len(char)):
            for letter in abc:
                word = ''.join((char[:i], letter, char[i:]))
                dict = search(word)
                if dict == {}:
                    continue
                else:
                    # adds [word,offset,dictionray
                    list_words.append([word, i, dict])

    return list_words

    def find_words_del(self, char):
        '''
       :param char: word with mistake
       :return: list of all possible words that appear in the dataset, with extra letter added
       the list is in format [word,offset, dictionary]
       '''
        i = 0
        abc = []
        orig = ''
        list_words = []
        dict = {}
        word = ''
        while (i != len(char)):
            word = char[:i] + char[i + 1:]
            dict = search(word)
            if dict == {}:
                continue
            else:
                # adds [word,offset,dictionray
                list_words.append([word, i, dict])

    return list_words

    def auto_complete(self, prefix):
        dict_merged = {}
        dict_word = {}
        changed = []
        add = []
        deleted = []
        for char in prefix:
            dict_merged = dict_word
            dict_word = search(char)
            if not dict_word == {}:
                if not dict_merged == {}:
                    dict_word = findIntersection(dict_merged, dict_word)
                    # if there is no intersection
                    if dict_word == {}:
                        self.auto_complete_correction(dict, prefix, char)
                else:
                    continue
            else:
                self.auto_complete_correction(dict1, prefix, char)
        return dict2

    def auto_complete_correction(self, dict1, prefix, char):
        add = self.find_words_add(self, char)
        deleted = self.find_words_add(self, char)
        changed = self.find_words_changed(self, char)


def auto_complete(prefix):
    word1=prefix[0]
    dict1=search(word1)
    word2=''
    for x in range(1, n+1):
       word2=prefix[x]
       dict2=search(word2)
       dict1=find_Intersection(dict1,dict2)
    return Autocomplete('unchanged',prefix,0,dict1)



