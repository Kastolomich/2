def main(x):
    a = x & 0b1111_1111_1111_11
    b = (x >> 14) & 0b1111_1111_11
    c = (x >> 24) & 0b1111_1
    d = (x >> 29) & 0b11
    e = (x >> 31) & 0b1
    result = b | (c << 10) | (d << 15) | (e << 17) | (a << 18)
    return result