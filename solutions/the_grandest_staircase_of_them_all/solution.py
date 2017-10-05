import json
import math

def calculate_steps(n):
    # pad size
    size = n + 1

    # create zero-filled matrix
    matrix = [[0 for _ in xrange(size)] for _ in xrange(size)]

    # base value is always padded and skipped
    matrix[0][0] = 1
    for prev in xrange(1, size):
        for left in xrange(0, size):
            matrix[prev][left] = matrix[prev - 1][left]
            if left >= prev:
                matrix[prev][left] += matrix[prev - 1][left - prev]

    return matrix[n][n] - 1

def answer(n):
    return calculate_steps(n)
