#! /usr/bin/env python3

from inputs_given import day4
from collections import Counter

# list<list<str>>
passphrases = [ row.split() for row in day4.split('\n') ]
valids = 0
for passphrase in passphrases:
    if len(passphrase) == len(set(passphrase)):
        valids += 1
print(valids)  # Part 1: 337

valids = 0
for passphrase in passphrases:
    previous_words = [Counter(passphrase[0])]  # init
    for word in passphrase[1:]:
        alphabets = Counter(word)
        if alphabets in previous_words:
            break
        else:
            previous_words.append(alphabets)
    else:
        # only if for loop does not break,
        # i.e. no anagrams
        valids += 1
print(valids)  # Part 2: 231
