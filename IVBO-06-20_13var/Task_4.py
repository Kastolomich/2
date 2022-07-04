from math import log10


def main(n):
    if n == 0:
        return 0.97
    elif n >= 1:
        return main(n-1) + log10(main(n-1)) ** 2 + 1
