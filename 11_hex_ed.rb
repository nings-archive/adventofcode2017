#! /usr/bin/env ruby

require 'ostruct'
require './inputs_given.rb'

class Grid
    # Axial coordinate system for hexagonal grids
    # x = 0 and y = 0 make a 60 degree angle rather than 90
    @@N  = OpenStruct.new;  @@N.x = 0;   @@N.y = 1
    @@NE = OpenStruct.new; @@NE.x = 1;  @@NE.y = 0
    @@SE = OpenStruct.new; @@SE.x = 1;  @@SE.y = -1
    @@S  = OpenStruct.new;  @@S.x = 0;   @@S.y = -1
    @@SW = OpenStruct.new; @@SW.x = -1; @@SW.y = 0
    @@NW = OpenStruct.new; @@NW.x = -1; @@NW.y = 1
    @@dir_map = { 'n' => @@N,
          'nw' => @@NW, 'ne' => @@NE,
          'sw' => @@SW, 'se' => @@SE,
                  's' => @@S }

    def initialize()
        @x, @y = 0, 0
        @furthest = 0
    end

    attr_reader :furthest

    def move(dir)
        # https://stackoverflow.com/a/19557156/
        @x = @x + @@dir_map[dir].x
        @y = @y + @@dir_map[dir].y
        @furthest = [ @furthest, self.solve ].max  # slow
    end

    def solve()
        steps = 0
        x = @x
        y = @y
        while x != 0 || y != 0
            steps += 1
            if y == 0
                x -= x / x.abs
            elsif x == 0
                y -= y / y.abs
            else
                x -= x / x.abs
                y -= y / y.abs
            end
        end
        return steps
    end

end

grid = Grid.new
path = Inputs::DAY11.split(',')
path.each { |dir| grid.move(dir) }
puts grid.solve  # Part 1: 720
puts grid.furthest  # Part 2: 1485
