from math import cos, ceil


def main(x):
    if x < 180:
        return x ** 2
    elif 180 <= x < 236:
        return x ** 4
    elif 236 <= x < 313:
        return 65 * x ** 5 + 27 * x ** 6 + ceil(x) ** 3
    elif x >= 313:
        return 49 * cos(27 * x ** 2 - 69 * x ** 3) ** 7 -\
               81 * x ** 2 - 80 * (1 + 7 * x ** 2) ** 6
