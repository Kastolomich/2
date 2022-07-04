def main(n):
    if n == 0:
        return 0.95
    elif n == 1:
        return -0.43
    elif n >= 2:
        return 93 * ((main(n-2) ** 3) / 40) ** 3 +\
               main(n-1) / 55
