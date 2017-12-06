#! /usr/bin/env python3

from given_inputs import day3

def get_steps(grid):
    ''' the quadrants are defined as:
            1 1 1 1 0
            2       0
            2       0
            2       0
            2 3 3 3 3 '''
    layer = get_layer(grid)
    width = get_width(layer)
    quad = 0
    quad_max = get_width(layer-1) ** 2 + (width - 1)
    while grid > quad_max:
        quad += 1
        quad_max += width - 1
    loc_in_quad = get_quad_loc(grid, width, quad)
    dist_from_centre = abs(loc_in_quad - (width-1)//2)
    return layer + dist_from_centre

def get_quad_loc(grid, width, quad):
    return grid - (width-2)**2 - quad*(width-1)

def get_layer(grid):
    ''' 17 16 15 14 13
        18  5  4  3 12
        19  6  1  2 11
        20  7  8  9 10
        21  22........
        grid [1] -> layer 0
        grid [2-9] -> layer 1
        grid [10-25] -> layer 2 '''
    layer = 0
    # size = (2n + 1)^2
    while get_width(layer) ** 2 < grid:
        layer += 1
    return layer

def get_width(layer):
    return layer * 2 + 1

print(get_steps(int(day3)))  # Part 1: 326
