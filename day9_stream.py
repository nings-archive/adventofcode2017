#! /usr/bin/env python3

import re

INPUT_FILE = 'inputs_given_day9.txt'
# match ! ; match one of any character
ignore_re  = '!.'
# match < ; match any num of any char except > ; match >
garbage_re = '<[^>]*>'  
# match anything that is not { or }
non_braces = '[^{}]'

with open(INPUT_FILE, 'r') as file:
    stream = file.read()

def remove_ignored(stream):
    return re.sub(ignore_re, '', stream)

def remove_garbage(stream):
    starting_length = len(stream)
    removed = re.sub(garbage_re, '', stream)
    return removed if len(removed) == starting_length \
        else remove_garbage(removed)

def remove_non_braces(stream):
    return re.sub(non_braces, '', stream)

stream_sanitised = remove_non_braces(remove_garbage(remove_ignored(stream)))

def count_score(stream, score_value):
    counters = {'{': 0, 'groups': 0}
    to_remove = [0]
    if stream == '':
        return 0
    else:
        for i in range(len(stream)):
            counters['{'] += 1 if stream[i] is '{' else -1
            if counters['{'] == 0:
                to_remove.append(i)
                to_remove.append(i+1)
                counters['groups'] += 1
        for i in to_remove:
            stream = stream[:i] + 'x' + stream[i+1:]
        return score_value * counters['groups'] \
            + count_score(re.sub('x', '', stream), score_value + 1)

print(count_score(stream_sanitised, 1))  # Part 1: 16869

def count_garbage(stream):
    stream = remove_ignored(stream)
    garbages = re.findall(garbage_re, stream)
    return sum([ len(garbage)-2 for garbage in garbages ])

print(count_garbage(stream))  # Part 2: 7284

