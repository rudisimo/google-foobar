import math

def calculate_tree_size(height):
    return long(math.pow(2, height) - 1)

def shift_right_zero_fill(value, bits):
    return (value & 0xffffffffL) >> bits

def find_parent(height, node):
    size = calculate_tree_size(height)
    if node == size:
        return -1

    previous = 0
    while True:
        size = shift_right_zero_fill(size, 1)
        left = previous + size
        right = left + size
        current = right + 1

        if left == node or right == node:
            return current

        if node > left:
            previous = left

    return 0

def answer(h, q):
    return [find_parent(h, n) for n in q]
