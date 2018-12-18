from string import ascii_uppercase
import re
from decode.ciphertexts import Ciphertext
from collections import Counter
import itertools
from collections import defaultdict

class VigenereCiphertext(Ciphertext):
    def repeated_patterns(self, n):
        results = defaultdict(list)
        iters = itertools.tee(self.raw_text, n)  # TODO: Update to work on current_text
        for i, iter in enumerate(iters):
            for _ in range(i):
                next(iter)  # Introduce correct iter offsets

        for i in range(len(self.raw_text) - n):
            pattern = ''.join(next(iter) for iter in iters)
            results[pattern].append(i)  # Yay for default dicts!

        results = {k: v for k, v in results.items() if len(v) > 1}

        return sorted(results.items(), key=lambda item: -len(item[1]))