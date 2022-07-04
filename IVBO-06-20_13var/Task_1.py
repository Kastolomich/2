from math import log


def main(y, z, x):
    res1 = ((58 - (y ** 2) / 92 - 10 * y ** 3) ** 7)
    res2 = log(42 * x ** 2 + 21 * z ** 3) ** 6
    res3 = ((56 * y + 61 * z ** 2) ** 5 - x) /\
           (z ** 3 - abs(x ** 3 + y ** 2 + y) ** 5)
    return res1 / 95 + res2 / 74 - res3
