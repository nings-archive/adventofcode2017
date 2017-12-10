#! /usr/bin/env python3

from inputs_given import day5

jumps = [ int(offset) for offset in day5.split('\n') ]
length = len(jumps)
index = 0
steps = 0

while index < length:
    jumps[index] += 1
    index += jumps[index] - 1
    steps += 1

print(steps)  # Part 1: 343467

jumps = [ int(offset) for offset in day5.split('\n') ]
length = len(jumps)
index = 0
steps = 0

while index < length:
    last_position = index
    index += jumps[last_position]
    if jumps[last_position] >= 3:
        jumps[last_position] -= 1
    else:
        jumps[last_position] += 1
    steps += 1

print(steps)  # Part 2: 24774780
