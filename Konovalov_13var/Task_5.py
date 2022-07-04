from math import ceil


def main(y, z, x):
    res = 0
    n = len(x)
    for i in range(1, n+1):
        res += ((90 * x[i-1] ** 3 + 25 *
                 z[n-ceil(i/2)] ** 2 + y[n-i]) ** 3) / 65
    return 66 * res
