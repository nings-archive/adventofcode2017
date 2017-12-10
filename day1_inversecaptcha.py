#! /usr/bin/env python3

from inputs_given import day1

def offset_by(seq, i):
    '''returns the seq, but starting from the ith index'''
    return seq[0+i:] + seq[:0+i]

def compare_and_sum(seq1, seq2):
    '''compares two seq and sums the numbers where they match'''
    result = 0
    seq_zipped = zip(seq1, seq2)
    for pair in seq_zipped:
        if pair[0] == pair[1]:
            result += int(pair[0])
    return result

print(compare_and_sum(
    day1, 
    offset_by(day1, -1)
))  # Part 1: 1177
print(compare_and_sum(
    day1,
    offset_by(day1, len(day1)//2)
))  # Part 2: 1060
