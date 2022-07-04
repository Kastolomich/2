def main(m, a, n):
    res1 = 0
    for c in range(1, m+1):
        res1 += 66 * (95 - c ** 3 - 17 * c ** 2) ** 5
    res2 = 0
    for k in range(1, m+1):
        for j in range(1, n+1):
            for c in range(1, a+1):
                res2 += (3 * c ** 2 - 74 * j ** 3 - k) ** 2 +\
                        1 + 12 * (1 + j) ** 4
    return res1 - res2


# Testing
print(main(6, 4, 3))
