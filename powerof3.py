# Determine if a given unsigned 32-bit number is a power of 3


def fill_powers():
    powers = set()
    x = 1
    while x <= 2**32:
        powers.add(x)
        x *= 3
    return powers

powers = fill_powers()


def is_power_of_3(i):
    return i in powers
