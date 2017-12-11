#! /usr/bin/env python3

from inputs_given import day10

class Pair:
    def __init__(self, *args):
        if len(args) == 0:
            self.head = self.tail = None
        elif len(args) == 2:
            self.head = args[0]
            self.tail = args[1]
        else:
            raise ValueError(
                "Pair expects 0 or 2 positional arguments only."
            )

    def is_empty(self):
        return self.head is None and self.tail is None

class LinkedList:
    def __init__(self, *args):
        self.head = Pair(None, None)
        def construct_list(values, anchor_pair):
            if values == ():
                pass
            else:
                anchor_pair.head = values[0]
                anchor_pair.tail = Pair()
                return construct_list(
                    values[1:],
                    anchor_pair.tail
                )
        construct_list(args, self.head)

    def loopify(self):
        def loop(anchor_pair):
            if anchor_pair.tail.is_empty():
                anchor_pair.tail = self.head
            else:
                return loop(anchor_pair.tail)
        loop(self.head)

    def index(self, i):
        def get_index(i, anchor_pair):
            if i == 0:
                return anchor_pair
            else:
                return get_index(i-1, anchor_pair.tail)
        return get_index(i, self.head)

    def set_new_head(self, new_head):
        self.head = new_head

    def __iter__(self):
        self.next_pair = self.head
        return self

    def __next__(self):
        if self.next_pair.is_empty():
            raise StopIteration
        to_return = self.next_pair
        self.next_pair = self.next_pair.tail
        return to_return

    def __repr__(self):
        repr_str = ''
        if self.head.is_empty():
            return repr_str
        else:
            repr_str += str(self.head.head) + ' '
        next_pair = self.head.tail
        while not next_pair.is_empty() and not next_pair is self.head:
            repr_str += str(next_pair.head) + ' '
            next_pair = next_pair.tail
        return repr_str

lengths = [ int(length) for length in day10.split(',') ]
circular_list = LinkedList(*[ i for i in range(256) ])
circular_list.loopify()

store_heads = []
skip_size = 0
for length in lengths:
    for i in range(length):
        store_heads.append(circular_list.index(i).head)
    for i in range(length):
        circular_list.index(i).head = store_heads.pop()
    circular_list.set_new_head(circular_list.index(length+skip_size))
    skip_size += 1


shifts_to_original_head = (
    256 - (sum(lengths) + (len(lengths) * (len(lengths) - 1)) // 2) % 256
)
circular_list.set_new_head(circular_list.index(shifts_to_original_head))

print(circular_list.index(0).head * circular_list.index(1).head)  # Part 1: 8536
