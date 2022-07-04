from math import exp, ceil


def main(x, z, y):
    res = 0
    n = len(z)
    for i in range(1, len(z) + 1):
        res += 9 * exp(y[n-i] ** 3 + z[ceil(i/4) - 1]
                       + 41 * x[n-ceil(i/3)] ** 2) ** 7
    return 17 * res


# Testing
print(main([0.45, 0.58, 0.07, 0.6],
[-0.86, 0.66, -0.48, 0.7],
[0.59, 0.24, -0.46, -0.95]))