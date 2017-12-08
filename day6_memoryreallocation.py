#! /usr/bin/env python3

from given_inputs import day6

configuration = [ int(bank) for bank in day6.split() ]
num_banks = len(configuration)
previous_states = []
cycles = 0

while configuration not in previous_states:
    previous_states.append(list(configuration))
    starting_index = configuration.index(max(configuration))
    max_blocks = configuration[starting_index]
    configuration[starting_index] = 0

    for _ in range(max_blocks):
        starting_index = starting_index + 1 \
            if starting_index is not num_banks - 1\
            else 0
        configuration[starting_index] += 1

    cycles += 1

print(cycles)  # Part 1: 6681
