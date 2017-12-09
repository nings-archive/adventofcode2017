#! /usr/bin/env python3

from given_inputs import day7

# the bottom program is the one not being held at all
# first generate a dict representing the data
# dict:programs < str:name -> tuple< int:weight, set<str:held> >
progs = {}  
for line in day7.split('\n'):
    temp = line.split(' -> ')
    temp_name_weight = temp[0].split()
    name = temp_name_weight[0]
    weight = temp_name_weight[1].replace('(', '').replace(')', '')
    holding = set(temp[1].split(', ')) if len(temp) == 2 else None

    progs[name] = (int(weight), holding)

# generate a Set of all programs that are held by some other program
progs_being_held = set()
for weight_holding in progs.values():
    if weight_holding[1] is not None:
        progs_being_held.update(weight_holding[1])

for name in progs.keys():
    if name not in progs_being_held:
        print(name)  # Part 1: eugwuhl
        break
