def main(x):
    a = x & 0b1111_1111_1111
    b = (x >> 12) & 0b1111_1111_1111
    c = (x >> 24) & 0b1111_111
    d = (x >> 31) & 0b1
    result = c | (b << 7) | (a << 19) | (d << 31)
    return result
