import itertools
import termcolor_util as tc


class Ciphertext:
    def __init__(self, text):
        self.raw_text = text
        self.reset()

    def reset(self):
        self.current_text = [(raw, tc.red(raw)) for raw in self.raw_text]

    @property
    def __str__(self):
        return ''.join(char[1] for char in self.current_text)

    def ngrams(self, n):
        pass

    def special_char_words(self):
        pass

    def get_freqs(self):
        pass