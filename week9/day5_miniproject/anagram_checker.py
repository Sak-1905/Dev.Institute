class AnagramChecker:
    def __init__(self, namelist):
        self.word_list = self.load_word_list(namelist)

    def load_word_list(self, namelist):
        with open(namelist.txt, 'r') as file:
            word_list = [word.strip() for word in file.readlines()]
        return word_list

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        sorted_word1 = sorted(word1.lower())
        sorted_word2 = sorted(word2.lower())
        return sorted_word1 == sorted_word2

    def get_anagrams(self, word):
        anagrams = []
        for entry in self.word_list:
            if self.is_anagram(word, entry) and word.lower() != entry.lower():
                anagrams.append(entry)
        return anagrams
