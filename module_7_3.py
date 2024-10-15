import re
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for file in file_names:
            self.file_names.append(file)
        # print(self.file_names)

    def get_all_words(self):
        all_words = {}
        for fname in self.file_names:
            # print(file)
            with open(fname, 'r', encoding='utf-8') as file:
                content = re.sub(r'[^\w\s]', '', str.lower(file.read()))
            words = content.split()
            all_words[fname] = words
        return all_words

    def find(self, word):
        position = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                position[key] = value.index(word.lower()) + 1

        return position

    def count(self, word):
        counter = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counter[value] = words_count

        return counter

finder2 = WordsFinder('test.txt', 'test_file2.txt', 'test_file_3.txt', 'products.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


