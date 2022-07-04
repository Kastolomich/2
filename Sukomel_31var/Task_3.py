def main(b, m, x, n):
    res1 = 0
    for i in range(1, m+1):
        for k in range(1, b+1):
            res1 += x ** 2 - 87 * k ** 7 -\
                    (70 * i ** 3) ** 3
    res2 = 0
    for i in range(1, m+1):
        for c in range(1, n+1):
            res2 += i ** 2 + c ** 4 + i ** 2
    return res1 + res2
