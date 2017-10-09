def answer(x, y):
    # find symmetric difference between the two sets
    diff = list(set(x) ^ set(y))
    # return fist item in output list
    return diff[0]
