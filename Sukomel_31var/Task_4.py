from math import log10


def main(n):
    if n == 0:
        return -0.91
    elif n >= 1:
        return log10(52 * main(n-1) ** 2 + 82) ** 2 + 88
