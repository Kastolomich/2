import struct
import pprint


def parse_d(data, pointer):
    d1, d2 = struct.unpack('>HB', data[pointer:pointer + 3])
    f3 = struct.unpack('>HH', data[pointer + 3:pointer + 7])
    d3 = list(struct.unpack(f'>{f3[0]}h', data[f3[1]:f3[1] + f3[0] * 2]))
    d4, d5, d6, d7 = struct.unpack('>hHHH', data[pointer + 7:pointer + 15])
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7}


def parse_c(data, pointer):
    c1 = list()
    c1.append(parse_d(data, pointer))
    c1.append(parse_d(data, pointer + 15))
    c2 = struct.unpack('>i', data[pointer + 30:pointer + 34])[0]
    return {'C1': c1, 'C2': c2}


def parse_b(data, pointer):
    f1 = struct.unpack('>H', data[pointer:pointer + 2])
    b1 = parse_c(data, f1[0])
    b2, b3 = struct.unpack('>bh', data[pointer + 2:pointer + 5])
    f4 = struct.unpack('>II', data[pointer + 5:pointer + 13])
    b4 = list(struct.unpack(f'>{f4[0]}f', data[f4[1]:f4[1] + f4[0] * 4]))
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}


def parse_a(data, pointer):
    f1 = struct.unpack('>H', data[pointer:pointer + 2])
    a1 = parse_b(data, f1[0])
    a2 = struct.unpack('>I', data[pointer + 2:pointer + 6])[0]
    f3 = struct.unpack('>HI', data[pointer + 6:pointer + 12])
    a3 = list(struct.unpack(f'>{f3[0]}f', data[f3[1]:f3[1] + f3[0] * 4]))
    a4, a5, a6, a7 = struct.unpack('>IQff', data[pointer + 12:pointer + 32])
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}


def main(data):
    return parse_a(data, 5)


# Testing
pprint.pprint(main(b'\x8cMSAS\x00i\x96:+1\x00\x02\x00\x00\x00v\xf6G\x8ah\x08\xb9\x02\xcar\x03\x9b'
                   b'\x02\xbfS\x9a\xab\xbe\xbe\xc0\xa9/\x82Q\x03^\x9d\xc7\x97)\xd2\xf2'
                   b'\x07\xefD\xe0@\x1a\xd8\xc0p4\xb6\xd0\x06:\xcc\xaf\\|\x00\x06\x00%\x16H'
                   b'\x9f\xf5`\x89l\xd5\x1cP\xa6\x00\x07\x001QY\x1aw\xa9\xdb\x99r\xb2\x9f\xf6'
                   b'\x9b>\x809\xb5\xbd\x9a:\x0c\x00?\xd1\x98\x16\x00\x00\x00\x02\x00\x00\x00a?X'
                   b'V1\xbe\xb6;3'))
