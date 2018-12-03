from string import ascii_uppercase
import re


def check_substitutions(substitutions):
    unsubbed = [letter for letter in ascii_uppercase if letter not in substitutions]
    unfound = [letter for letter in ascii_uppercase if letter not in substitutions.values()]
    if len(unsubbed) != len(unfound):
        raise ValueError('ERROR: Multiple assignments in substitution dictionary')
    print('Unsubstituted Letters: {}'.format(''.join(unsubbed)))
    print('Not Yet Found Letters: {}'.format(''.join(unfound)))
    return len(unsubbed)


def substitute(text, substitutions):
    return ''.join(substitutions.get(letter, letter) for letter in text)


def ngrams(text, n):
    words = re.sub('^[A-Z ]', '', text).split(' ')
    return {word: text.count(word) for word in words if len(word) == n}


def special_char_words(text):
    words = re.sub('^[A-Z ’\'`\-]', '', text).split(' ')
    return {word: text.count(word) for word in words if re.search('’|`|\'|-', word)}