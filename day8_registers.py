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

    try:
        reg_val2 = reg_lookup[reg2]
    except KeyError:
        reg_lookup[reg2] = reg_val2 = 0

    if evaluate_conditional(reg_val2, op2, val2):
        evaluate_operation(reg1, op1, val1)

def evaluate_operation(reg, op, val):
    if op == 'inc':
        try:
            reg_lookup[reg] += val
        except KeyError:
            reg_lookup[reg] = val
    elif op == 'dec':
        try:
            reg_lookup[reg] -= val
        except KeyError:
            reg_lookup[reg] = -val

def evaluate_conditional(reg_val, op, val):
    if op == '==':
        return reg_val == val
    elif op == '!=':
        return reg_val != val
    elif op == '<=':
        return reg_val <= val
    elif op == '>=':
        return reg_val >= val
    elif op == '<':
        return reg_val < val
    elif op == '>':
        return reg_val > val
    else:
        pass

max_values = []
for instruction in instructions:
    evaluate_statement(instruction)
    max_values.append(max(list(reg_lookup.values())))
print(max(list(reg_lookup.values())))  # Part 1: 3745
print(max(max_values))  # Part 2: 4644
