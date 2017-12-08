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

class Grid:
    mem = {}
    DIRS = {'right': 0, 'up'  : 1, 'left' : 2, 'down' : 3}

    def __init__(self):
        self.coord = (0, 0)
        self.value = 1
        self.layer = 0
        self.dir = Grid.DIRS['down']
        Grid.mem[self.coord] = self.value

    def __next__(self):
        if self.coord == (0, 0):
            self.coord = (1, 0)
            self.value = self.get_value()
            Grid.mem[self.coord] = self.value
            self.layer += 1
            self.dir = Grid.DIRS['up']
        elif self.is_at_boundary() and self.dir is not Grid.DIRS['right']:
            self.dir = self.get_next_direction()
            self.coord = self.get_next_coord()
            self.value = self.get_value()
            Grid.mem[self.coord] = self.value
        elif self.is_at_boundary() and self.dir is Grid.DIRS['right']:
            self.coord = self.get_next_coord()
            self.value = self.get_value()
            Grid.mem[self.coord] = self.value
            self.layer += 1
            self.dir = Grid.DIRS['up']
        else:
            self.coord = self.get_next_coord()
            self.value = self.get_value()
            Grid.mem[self.coord] = self.value
        
    def is_at_boundary(self):
        ''' anything more than this value is out of boundary '''
        if self.dir is Grid.DIRS['right']:
            return self.coord[0] == self.layer
        elif self.dir is Grid.DIRS['up']:
            return self.coord[1] == self.layer
        elif self.dir is Grid.DIRS['left']:
            return self.coord[0] == -self.layer
        elif self.dir is Grid.DIRS['down']:
            return self.coord[1] == -self.layer
        else:
            pass

    def get_next_coord(self):
        if self.dir is Grid.DIRS['right']:
            return self.coord[0] + 1, self.coord[1]
        elif self.dir is Grid.DIRS['up']:
            return self.coord[0], self.coord[1] + 1
        elif self.dir is Grid.DIRS['left']:
            return self.coord[0] - 1, self.coord[1]
        elif self.dir is Grid.DIRS['down']:
            return self.coord[0], self.coord[1] - 1
        else:
            pass

    def get_next_direction(self):
        if self.dir is Grid.DIRS['right']:
            return Grid.DIRS['up']
        elif self.dir is Grid.DIRS['up']:
            return Grid.DIRS['left']
        elif self.dir is Grid.DIRS['left']:
            return Grid.DIRS['down']
        elif self.dir is Grid.DIRS['down']:
            return Grid.DIRS['right']
        else:
            pass

    def get_value(self):
        result = 0
        for coord in self.get_adjacent_coords():
            try:
                result += Grid.mem[coord]
            except KeyError:
                pass
        return result

    def get_adjacent_coords(self):
        x, y = self.coord[0], self.coord[1]
        return \
            [ (x-1, y+1), (  x, y+1), (x+1, y+1),
              (x-1, y  ),             (x+1, y  ),
              (x-1, y-1), (  x, y-1), (x+1, y-1) ]

grid = Grid()
while grid.value < int(day3):
    next(grid)

print(grid.value)  # Part 2: 363010
