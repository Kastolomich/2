from math import ceil


def main(m, n, y, a):
    res1 = 0
    for k in range(1, n+1):
        for i in range(1, m+1):
            res1 += 60 * y + i ** 2 + 1 + k ** 5
    res2 = 0
    for j in range(1, a+1):
        for c in range(1, m+1):
            res2 += y ** 6 + ceil(c) ** 4 + (67 - y ** 2 - 9 * j) ** 2
    return res1 + res2
