#! /usr/bin/env python3

from given_inputs import day2

def multilinestr_to_list_of_list_of_int(string):
    ''' splits a multi-line string into a list of strings by newline delimiter,
        then splits said string entries by tab delimiter '''
    return [ list(map(int, row.split('\t'))) for row in string.split('\n') ]

spreadsheet_list = multilinestr_to_list_of_list_of_int(day2)
min_max_list = [ (min(row), max(row)) for row in spreadsheet_list ]
checksum = sum([ min_max[1] - min_max[0] for min_max in min_max_list ])

print(checksum) # 32020

def is_evenly_divisible(int1, int2):
    return int1 / int2 % 1 == 0 if int1 > int2 \
            else int2 / int1 % 1 == 0

def find_evenly_divisibles(row):
    for i in range(len(row)):
        anchor = row[i]
        for num in row[i+1:]:
            if is_evenly_divisible(anchor, num):
                return anchor, num

def evenly_divide(ints):
    return ints[0] // ints[1] if ints[0] > ints[1] \
            else ints[1] // ints[0]

result = 0
for row in spreadsheet_list:
    evenly_divisibles = find_evenly_divisibles(row)
    result += evenly_divide(evenly_divisibles)

print(result)
