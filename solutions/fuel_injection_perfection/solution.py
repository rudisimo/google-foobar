def answer(n):
    n = long(n)

    # define lookup table
    lookup_table = { 1L: 0, 2L: 1 }

    def calculate_steps(n):
        # return memoized value in lookup table
        if n in lookup_table:
            return lookup_table[n]

        # handle safety control limitations (optimized)
        if n & 1:
            # odd numbers have an extra operation due to constraint
            lookup_table[n] = min(calculate_steps((n + 1) >> 1) + 2,
                                  calculate_steps((n - 1) >> 1) + 2)
        else:
            # even numbers add a single operation
            lookup_table[n] = calculate_steps(n >> 1) + 1

        return lookup_table[n]

    # calculate number of steps
    return calculate_steps(n)