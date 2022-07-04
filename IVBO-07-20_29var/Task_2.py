from math import floor


def main(x):
    if x < 174:
        return floor(x ** 2) + 66 * (95 - x ** 3 - 17 * x ** 2) ** 3 + x ** 5
    elif 174 <= x < 270:
        return 0.11 - 42 * ((x ** 3) / 42) ** 5 - 42\
               * (x ** 2 - x / 87 - 1) ** 4
    elif x >= 270:
        return 1 - 62 * (x - 32 * x ** 2) ** 3


# Testing
print(main(211))
