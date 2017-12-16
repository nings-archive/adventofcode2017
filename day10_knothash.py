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

    def unloopify(self):
        if self.head.is_empty():
            pass
        else:
            next_pair = self.head.tail
            while not next_pair.tail is self.head:
                next_pair = next_pair.tail
            next_pair.tail = Pair()

    def index(self, i):
        i = i % self.__len__()
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

    def __len__(self):
        if self.head.is_empty():
            return 0
        len_counter = 1
        next_pair = self.head.tail
        while not next_pair.is_empty() and not next_pair is self.head:
            len_counter += 1
            next_pair = next_pair.tail
        return len_counter

lengths = [ int(length) for length in day10.split(',') ]
circular_list = LinkedList(*[ i for i in range(256) ])
circular_list.loopify()

original_head = circular_list.head
store_heads = []
skip_size = 0
for length in lengths:
    for i in range(length):
        store_heads.append(circular_list.index(i).head)
    for i in range(length):
        circular_list.index(i).head = store_heads.pop()
    circular_list.set_new_head(circular_list.index(length+skip_size))
    skip_size += 1

print(original_head.head * original_head.tail.head)  # Part 1: 8536

lengths_ascii = [ ord(char) for char in day10 ]
lengths_ascii.extend([17, 31, 73, 47, 23])
lengths_ascii *= 64
circular_list = LinkedList(*[ i for i in range(256) ])
circular_list.loopify()
original_head = circular_list.head
store_heads = []
skip_size = 0
for length in lengths_ascii:
    for i in range(length):
        store_heads.append(circular_list.index(i).head)
    for i in range(length):
        circular_list.index(i).head = store_heads.pop()
    circular_list.set_new_head(circular_list.index(length+skip_size))
    skip_size += 1

circular_list.set_new_head(original_head)
circular_list.unloopify()
list_of_values = [ pair.head for pair in circular_list ]

def sparse_to_dense(sparse):
    result = []
    for i in range(16):
        result.append(operate(sparse[i*16:(i+1)*16]))
    return result

def operate(xs):
    if xs == []:
        return 0
    else:
        return xs[0] ^ operate(xs[1:])

dense_hash = sparse_to_dense(list_of_values)
knot_hash_nums = [ str(hex(num)[2:]) for num in dense_hash ]
knot_hash = ''.join(knot_hash_nums)
print(knot_hash)  # Part 2: aff593797989d665349efe11bb4fd99b
