IMPOSSIBLE = "impossible"
THRESHOLD = 100L

def multiplier(a, b):
    difference = a - b
    multiplier = (difference / b) + 1
    return multiplier

def answer(M, F):
    step = 0L
    mach = long(M)
    facula = long(F)

    try:
        if mach == facula or mach <= 0L or facula <= 0L:
            raise ValueError('Incorrect number of bomb types encountered')

        while True:
            if mach <= 0L or facula <= 0L:
                raise ValueError('Zero or less bomb types encountered')

            # optimize for large integers
            if mach > THRESHOLD or facula > THRESHOLD:
                if mach > facula:
                    mul = multiplier(mach, facula)
                    mach -= facula * mul
                    step += mul
                elif facula > mach:
                    mul = multiplier(facula, mach)
                    facula -= mach * mul
                    step += mul
                else:
                    raise StopIteration('Same number of bomb types encountered')
            else:
                if mach > facula:
                    mach -= facula
                elif facula > mach:
                    facula -= mach
                else:
                    raise StopIteration('Same number of bomb types encountered')
                step += 1L
    except:
        pass

    if mach == 1L and facula == 1L and step >= 0:
        return str(step)
    else:
        return IMPOSSIBLE
