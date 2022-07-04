def main(n, a, m):
    res1 = 0
    for j in range(1, m+1):
        for c in range(1, a+1):
            for k in range(1, n+1):
                res1 += k ** 3 + ((91 * c ** 2 -
                                   (j ** 3) / 25) ** 5) /\
                        14 + 22 * k ** 2
    return res1
