from string import ascii_uppercase
import re
from decode.ciphertexts import Ciphertext
from collections import Counter


class SubstitutionCiphertext(Ciphertext):
    def __init__(self, text):
        super().__init__(text)

    def substitute(self, substitutions):
        for i, letter in enumerate(self.raw_text):
            if letter in substitutions.map:
                self.current_text[i] = (substitutions.map[letter], 'sub')
        print(self)

    def get_freqs(self):
        freqs = Counter(char[0] for char in self.current_text if char[1] == 'raw')
        return freqs


class Substitution:
    def __init__(self):
        self.map = {}

    def add(self, raw, sub):
        self.map[raw] = sub

    def check(self):
        unsubbed = [letter for letter in ascii_uppercase if letter not in self.map]
        unfound = [letter for letter in ascii_uppercase if letter not in self.map.values()]
        if len(unsubbed) != len(unfound):
            raise ValueError('ERROR: Multiple assignments in substitution dictionary')
        print('Unsubstituted Letters: {}'.format(''.join(unsubbed)))
        print('Not Yet Found Letters: {}'.format(''.join(unfound)))
        return len(unsubbed)


def special_char_words(text):
    words = re.sub('^[A-Z ’\'`\-]', '', text).split(' ')
    return {word: text.count(word) for word in words if re.search('’|`|\'|-', word)}