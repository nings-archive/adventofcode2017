#! /usr/bin/env python3

from given_inputs import day1

def inverse_captcha_pt1(seq):
    '''hold the last char in a variable,
       check the current char with the last
       if the same, add to result'''
    last = seq[-1]
    result = 0
    for char in seq:
        if char == last:
            result += int(char)
        last = char
    return result

def inverse_captcha_pt2(seq):
    '''create another sequence that starts from the middle
       zip it with the original
       iterate through the zip, comparing tuple entries
       if the same, add to result'''
    seq_len = len(seq)
    seq_from_halfway = seq[seq_len//2:] + seq[:seq_len//2]
    zipped = zip(seq, seq_from_halfway)
    result = 0
    for pair in zipped:
        if pair[0] == pair[1]:
            result += int(pair[0])
    return result

print(inverse_captcha_pt1(day1))
print(inverse_captcha_pt2(day1))
