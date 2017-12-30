#! /usr/bin/env python3

from inputs_given import day8

# list<list<str>>
instructions = [ row.split() for row in day8.split('\n') ]

reg_lookup = {}

def evaluate_statement(statement):
    reg1 = statement[0]
    op1  = statement[1]
    val1 = int(statement[2])
    reg2 = statement[4]
    op2  = statement[5]
    val2 = int(statement[6])
    try_init_regs(reg1, reg2)

    if evaluate_conditional(reg2, op2, val2):
        evaluate_operation(reg1, op1, val1)

def try_init_regs(*args):
    for reg in args:
        try:
            reg_lookup[reg]
        except KeyError:
            reg_lookup[reg] = 0

def evaluate_operation(reg, op, val):
    exec("reg_lookup['{}'] {} {}".format(
        reg,
        '+=' if op == 'inc' else '-=',
        val
    ))

def evaluate_conditional(reg, op, val):
    return eval('{} {} {}'.format(reg_lookup[reg], op, val))

max_values = []
for instruction in instructions:
    evaluate_statement(instruction)
    max_values.append(max(list(reg_lookup.values())))
print(max(list(reg_lookup.values())))  # Part 1: 3745
print(max(max_values))  # Part 2: 4644
