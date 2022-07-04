from math import sqrt


def main(z, x):
    res1 = (z ** 3 - abs(x) ** 4) / (89 * (49 * x ** 2 - z ** 3) ** 5)
    res2 = sqrt((34 * (48 * z ** 3 + 36 *
                       x ** 2 + 3) ** 5) / (52 * z ** 3 + x ** 4))
    return res1 + res2
