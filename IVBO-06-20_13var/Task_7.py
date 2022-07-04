def main(x):
    a = x & 0b1111_1111_1111_11
    b = (x >> 14) & 0b1111_1111_1111
    c = (x >> 26) & 0b111
    d = (x >> 29) & 0b11
    e = (x >> 31) & 0b1
    result = c | (d << 3) | (b << 5) | (e << 17) | (a << 18)
    return result
