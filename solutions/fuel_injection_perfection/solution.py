def answer(n):
    num = long(n)
    steps = 0

    # exit quickly on edge cases
    if num < 1 or len(n) > 309:
        return 0

    # handle quantum antimatter safety control
    if num & 1 == 1:
        num += 1       # pad to an even number
        steps += 1     # this operation counts towards our goal

    # calculate the number of operations
    while num > 1:
        num >>= 1      # optimize division by using shift-right operation
        steps += 1     # increase number of operations

    return steps