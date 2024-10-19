class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(char, ' ')
                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            try:
                position = words.index(word.lower()) + 1
                result[file_name] = position
            except ValueError:
                pass
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result

# Пример использования
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())
    print(finder.find('child'))
    print(finder.count('child'))


''' test_file.txt
Monday’s Child

Monday’s child is fair of face
Tuesday’s child is full of grace
Wednesday’s child is full of woe
Thursday’s child has far to go,
Friday’s child is loving and giving,
Saturday’s child works hard for a living,
And the child that is born on the Sabbath day
Is bonny and blithe, and good and gay.

Mother Goose
'''