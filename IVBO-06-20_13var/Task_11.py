import struct
import pprint


def parse_e(data, pointer):
    e1, e2 = struct.unpack('<HB', data[pointer:pointer + 3])
    return {'E1': e1, 'E2': e2}


def parse_d(data, pointer):
    d1 = list(struct.unpack('<5B', data[pointer:pointer + 5]))
    d2, d3, d4 = struct.unpack('<Bih', data[pointer + 5:pointer + 12])
    d5 = list(struct.unpack('<2I', data[pointer + 12:pointer + 20]))
    d6, d7 = struct.unpack('<hd', data[pointer + 20:pointer + 30])
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7}


def parse_c(data, pointer):
    c1, c2, c3, c4, c5, c6 = struct.unpack('<qiQBhq',
                                           data[pointer:pointer + 31])
    c7 = list()
    c7.append(parse_d(data, pointer + 31))
    c7.append(parse_d(data, pointer + 61))  # pointer = 91
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6, 'C7': c7}


def parse_b(data, pointer):
    f1 = struct.unpack('<H', data[pointer:pointer + 2])
    b1 = parse_c(data, f1[0])
    b2 = struct.unpack('<H', data[pointer + 2:pointer + 4])[0]
    f3 = struct.unpack('<IH', data[pointer + 4:pointer + 10])
    b3 = list(struct.unpack(f'<{f3[0]}d', data[f3[1]:f3[1] + f3[0] * 8]))
    b4 = parse_e(data, pointer + 10)
    b5 = list(struct.unpack('<5B', data[pointer + 13:pointer + 18]))
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5}


def parse_a(data, pointer):
    a1, a2 = struct.unpack('<hH', data[pointer:pointer + 4])
    a3 = parse_b(data, pointer + 4)
    a4 = struct.unpack('<Q', data[pointer + 22:pointer + 30])[0]
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}


def main(data):
    return parse_a(data, 5)


# Testing
pprint.pprint(main(b'MIZG\x10E\x16^\xda#\x00\x18\xcd\x03\x00\x00\x00~\x00\xfb}\xf7\xd4^'
                   b'\x83\x14C\xdb\xf9[+\xb0\x18\x86\x81\xfe\x0e\xfb0P\x08\x1c2[\xfb\x82\x95a'
                   b'g<w\x1a\xff*\xa8Im\xf9\xf8M\xca\xfc\xe0&S\x86E\xefNF8\xbc\xfaf}\xe0'
                   b'\xfc\xc2\xfb\x82\x82\x00va\xb5\xd9\x91D\x80\xa0\xf6h\xd2\x16\xd7\xbf'
                   b'\x874 \x02yC\x9d\x0ei\x94\xa7\xe8+,\xf5\x06X\x13\xb8\x1e\\Q\\\xfa'
                   b"\x08\r\x9d\x9b\xd6?\xa0\xcd'XE\xca\xbd?\n\x1e\xfe&\xb7,\xe7\xbf\xde\xb6\t+Fb"
                   b'\xe0\xbf'))
