import termcolor_util as tc
from string import ascii_uppercase


class Ciphertext:
    def __init__(self, text):
        self.raw_text = text
        self.colours = {'raw': tc.red, 'sub': tc.green}
        self.current_text = [(raw, 'raw') for raw in self.raw_text]

    def char_to_string(self, char):
        return self.colours[char[1]](char[0])

    def text_to_string(self, text):
        return ''.join(self.char_to_string(char) for char in text)

    def __repr__(self):
        return ''.join(self.char_to_string(char) for char in self.current_text)

    def ngrams(self, n):
        last_space = 0
        results = {}
        for i, char in enumerate(self.current_text):
            if char[0] == ' ':
                if i - last_space == n + 1:
                    word = self.text_to_string(self.current_text[last_space + 1:i])
                    results[word] = results.get(word, 0) + 1
                last_space = i
        for word in results:
            print('{}   -   {}'.format(word, results[word]))

    def special_char_words(self):
        last_space = 0
        results = {}
        for i, char in enumerate(self.current_text):
            if char[0] == ' ':
                word = self.current_text[last_space + 1:i]
                if not all(char[0] in (ascii_uppercase + ';:,.') for char in word):
                    word = self.text_to_string(word)
                    results[word] = results.get(word, 0) + 1
                last_space = i
        for word in results:
            print('{}   -   {}'.format(word, results[word]))

    def doubles(self):
        results = {}
        for i in range(len(self.current_text) - 1):
            letter = self.char_to_string(self.current_text[i])
            next_letter =  self.char_to_string(self.current_text[i + 1])
            if letter == next_letter:
                results[2 * letter] = results.get(2 * letter, 0) + 1

        for double in results:
            print('{}   -   {}'.format(double, results[double]))