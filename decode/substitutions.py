from string import ascii_uppercase
import re
from decode.ciphertexts import Ciphertext
import termcolor_util as tc


class SubstitutionCiphertext(Ciphertext):
    def __init__(self, text):
        super().__init__(text)

    def substitute(self, substitutions):
        for i, letter in enumerate(self.raw_text):
            if letter in substitutions:
                self.current_text[i] = (substitutions[letter], tc.green(substitutions[letter]))


def check_substitutions(substitutions):
    unsubbed = [letter for letter in ascii_uppercase if letter not in substitutions]
    unfound = [letter for letter in ascii_uppercase if letter not in substitutions.values()]
    if len(unsubbed) != len(unfound):
        raise ValueError('ERROR: Multiple assignments in substitution dictionary')
    print('Unsubstituted Letters: {}'.format(''.join(unsubbed)))
    print('Not Yet Found Letters: {}'.format(''.join(unfound)))
    return len(unsubbed)


def ngrams(text, n):
    words = re.sub('^[A-Z ]', '', text).split(' ')
    return {word: text.count(word) for word in words if len(word) == n}


def special_char_words(text):
    words = re.sub('^[A-Z ’\'`\-]', '', text).split(' ')
    return {word: text.count(word) for word in words if re.search('’|`|\'|-', word)}