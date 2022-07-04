import struct
import pprint


def parse_d(data, pointer):
    f1 = struct.unpack('>II', data[pointer:pointer + 8])
    d1 = list(struct.unpack(f'>{f1[0]}d', data[f1[1]:f1[1] + f1[0] * 8]))
    d2, d3, d4, d5, d6, d7, d8 = struct.unpack('>fHfBHQH',
                                               data[pointer + 8:pointer + 31])
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7, 'D8': d8}


def parse_c(data, pointer):
    c1, c2 = struct.unpack('>BB', data[pointer:pointer + 2])
    c3 = list(struct.unpack('>4H', data[pointer + 2:pointer + 10]))
    return {'C1': c1, 'C2': c2, 'C3': c3}


def parse_b(data, pointer):
    f1 = struct.unpack('>II', data[pointer:pointer + 8])
    b1 = ''.join(map(str, struct.unpack(f'>{f1[0]}c',
                                        data[f1[1]:f1[1] + f1[0]])))
    b1 = b1.replace('\'', '')
    b1 = b1[1::2]
    b2 = parse_c(data, pointer + 8)
    return {'B1': b1, 'B2': b2}


def parse_a(data, pointer):
    f1 = struct.unpack('>2I', data[pointer:pointer + 8])
    a1 = list()
    for i in range(2):
        a1.append(parse_b(data, f1[i]))
    a2, a3 = struct.unpack('>BH', data[pointer + 8:pointer + 11])
    a4 = parse_d(data, pointer + 11)
    a5 = struct.unpack('>b', data[pointer + 42:pointer + 43])[0]
    return {'A1': a1, 'A2': a2, 'A3': a3,
            'A4': a4, 'A5': a5}


def main(data):
    return parse_a(data, 5)


# Testing
pprint.pprint(main(b'QAIZN\x00\x00\x003\x00\x00\x00G7\xc3\xd5\x00\x00\x00\x05\x00\x00\x00Y'
                   b'>\xd5\xb9\xb3\xbb\x08\xbf}%\xecN\x0c>84\xf7A)\x88p\xda\xac+\x93eqm\x00'
                   b'\x00\x00\x03\x00\x00\x000\x12:p\x12\xf3\x94\xe2\xf2\xd5\xe4cr\x00'
                   b"\x00\x00\x02\x00\x00\x00E\xa8$N|\x1a\xf7\xcf'n%\xbf\xe2)\xc2\xbd\x86\xb4"
                   b'\xee\xbf\xd1/\xe5G\xc6n\xfc?\xd7e{\xcej\xb9\\\xbf\xcd\x82\xe3\x95s\x12'
                   b'\x18\xbf\xea\x93\x1c\xb2\x06\x1f\xec'))
