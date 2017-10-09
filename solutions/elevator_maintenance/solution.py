def answer(l):
    # sort using simple semver comparison function
    l.sort(key=lambda v: map(int, v.split('.')))
    # return sorted list
    return l
