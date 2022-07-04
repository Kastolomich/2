from math import ceil


def main(z, x):
    res = 0
    n = len(x)
    for i in range(1, n+1):
        res += 65 * (7 * z[n-i] - 69 * x[i-1] ** 3 - 1)
    return res
