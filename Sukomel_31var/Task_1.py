from math import asin


def main(y, x):
    res1 = 76 * asin(x - y ** 3 - 36 * x ** 2) ** 3 - 2
    res2 = (y ** 2 - x ** 3 - 1) / 49
    return res1 + res2
