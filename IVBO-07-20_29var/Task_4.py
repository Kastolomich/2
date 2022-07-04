def main(n):
    if n == 0:
        return -0.09
    elif n == 1:
        return -0.70
    elif n >= 2:
        return main(n-2) ** 4 - main(n-1) ** 3 - 1


# Testing
print(main(9))
