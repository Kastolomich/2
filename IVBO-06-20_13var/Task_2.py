from math import ceil


def main(z):
    if z < -4:
        return ceil(z)
    elif -4 <= z < 74:
        return 73 * z - 75 * z ** 6
    elif z >= 74:
        return (87 * z) ** 2 + 53 * z ** 3 + z ** 7
