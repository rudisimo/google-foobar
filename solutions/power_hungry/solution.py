def answer(xs):
    # handle simple edge cases
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])

    # split input into positive/negative lists
    positive_numbers = []
    negative_numbers = []
    for n in xs:
        if n > 0: positive_numbers.append(n)
        elif n < 0: negative_numbers.append(n)

    # cache list counts
    positive_count = len(positive_numbers)
    negative_count = len(negative_numbers)

    # handle single negative panel edge case
    if negative_count == 1 and positive_count == 0:
        return str(0)

    # handle all zeros edge case
    if negative_count == 0 and positive_count == 0:
        return str(0)

    # calculate positive power output
    power_output = 1L
    for n in positive_numbers:
        power_output *= n

    # remove "largest" negative panel in odd arrangements
    if negative_count % 2 == 1:
        negative_numbers.remove(max(negative_numbers))

    # calculate negative power output
    for n in negative_numbers:
        power_output *= n

    return str(power_output)
