def main(x):
    a = x & 0b1111_1111
    b = (x >> 8) & 0b1
    c = (x >> 9) & 0b1111_11
    d = (x >> 15) & 0b1111_1111_1111_11
    e = (x >> 29) & 0b11
    f = (x >> 31) & 0b1
    result = e | (d << 2) | (a << 16) | (f << 24) | (b << 25) | (c << 26)
    return result
