#! /usr/bin/env ruby

require 'set'
require './inputs_given.rb'

programs = Inputs::DAY12.split("\n")
program_hash = {}  # hash< int => List<int> >
programs.each { |program|
    name_and_conn = program.split(' <-> ')
    name = name_and_conn[0].to_i
    conn = name_and_conn[1].split(', ')
                           .map! { |p| p.to_i }
    program_hash[name] = conn
}

def count_group(program_hash, start=nil)
    inspect_queue, inspected, group = Set.new, Set.new, Set.new
    inspect_queue.add(
        start == nil ? program_hash.keys[0] : start
    )

    while inspect_queue.length != 0 do
        prog = inspect_queue.to_a[0]
        group.add(prog)
        program_hash[prog].each { |p|
            unless inspected.member?(p)
                inspect_queue.add(p)
            end
        }
        inspected.add(prog)
        inspect_queue.delete(prog)
    end

    return group
end

def remove_keys(keys, hash)
    keys.each { |k| hash.delete(k) }
end

puts count_group(program_hash, 0).length  # Part 1: 141

groups = 0
while program_hash.length != 0
    group = count_group(program_hash)
    remove_keys(group, program_hash)
    groups += 1
end
puts groups  # Part 2: 171
