#! /usr/bin/env python3

from inputs_given import day7
# from inputs_given import day7test as day7  # small testcase

# the bottom program is the one not being held at all
# first generate a dict representing the data
# dict:programs < str:name -> tuple< int:weight, set<str:held> >
prog_lookup = {}  
for line in day7.split('\n'):
    temp = line.split(' -> ')
    temp_name_weight = temp[0].split()
    name = temp_name_weight[0]
    weight = temp_name_weight[1].replace('(', '').replace(')', '')
    holding = set(temp[1].split(', ')) if len(temp) == 2 else None

    prog_lookup[name] = (int(weight), holding)

# generate a Set of all programs that are held by some other program
progs_being_held = set()
for weight_holding in prog_lookup.values():
    # tuple:weight_holding <int:weight, set<str:name>||None >
    if weight_holding[1] is not None:
        progs_being_held.update(weight_holding[1])

for name in prog_lookup.keys():
    if name not in progs_being_held:
        print(name)  # Part 1: eugwuhl
        break

class Program:
    lookup_table = prog_lookup

    def __init__(self, name):
        # tuple:weight_holding <int:weight, set<str:name>||None >
        weight_holding = Program.lookup_table[name]
        self.name = name
        self.weight = weight_holding[0]
        self.holding = []
        # if this program is holding other programs...
        if weight_holding[1] is not None:
            for prog_name in weight_holding[1]:
                self.holding.append(Program(prog_name))

    def __repr__(self):
        names_held = [ progs.name for progs in self.holding ]
        return '{} ({}) -> {}'.format(self.name, self.weight, names_held)

def find_unbalanced(program):
    ''' start checking from the deepest branches,
        if a check passes, compress the branch into one prog '''
    for prog in program.holding:
        find_unbalanced(prog)
    weight_lookup = {}
    for prog in program.holding:
        weight_lookup[prog.name] = prog.weight
    if not odd_one_out(list(weight_lookup.values())) == []:
        print(weight_lookup)  # ...just look for the first print
    program.weight += sum(list(weight_lookup.values()))

def odd_one_out(weights):
    ''' list<int:weights> -> bool'''
    if weights == []:
        return []
    else:
        sample_weight = weights[0]
        weights_not_sample_weight = filter(
            lambda m: m != sample_weight,
            weights
        )
        return list(weights_not_sample_weight)

eugwuhl = Program('eugwuhl')
print(find_unbalanced(eugwuhl))  # Part 2: 420 (some steps required lel)
