from math import log


def main(y):
    if y < -6:
        return (17 * y ** 2 - 75 - 49 * y ** 3) ** 4
    elif -6 <= y < 28:
        return 68 * (y ** 3 - 15 * y ** 2) ** 4 - 1
    elif 28 <= y < 73:
        return 70 * log(y) ** 3 + 61 * y ** 2
    elif y >= 73:
        return 46 - 92 * y ** 6 - 81 * (y - y ** 2) ** 2
