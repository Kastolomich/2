from math import ceil, tan


def main(y, z, x):
    res = 0
    n = len(x)
    for i in range(1, n+1):
        res += (tan(x[ceil(i/4)-1] ** 2 - 56 * z[i-1] - y[n-i] ** 3)) / 64
    return res * 98
