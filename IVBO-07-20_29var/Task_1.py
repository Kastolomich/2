from math import sin


def main(x, z, y):
    res1 = (abs(x + 10 * x ** 3) ** 5 + ((y ** 2) / 22 - (z ** 3) / 81) ** 7) / \
           (65 * ((x ** 3) / 49 - y ** 2 - 18 * z) ** 5)
    res2 = sin(z ** 3 - y / 73 - (x ** 2) / 51)
    res3 = 34 * (1 + 76 * y + 77 * x ** 2) ** 7
    return res1 + res2 - res3


# Testing
print(main(-0.95, -0.66, -0.59))
