from decode.ciphertexts import Ciphertext


class CaesarCiphertext(Ciphertext):
    def rotate(self, n):
        out = ''
        for char in self.raw_text:
            if char == ' ':
                out += ' '
            else:
                out += chr(ord('A') + (ord(char) - ord('A') + n) % 26)
        return out

    def brute(self):
        for i in range(26):
            print('{}   -   {}'.format(i, self.rotate(i)))