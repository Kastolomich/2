import struct
import pprint


def parse_d(data, pointer):
    d1 = list(struct.unpack('<4H', data[pointer:pointer + 8]))
    d2 = struct.unpack('<H', data[pointer + 8:pointer + 10])[0]
    f3 = struct.unpack('<HI', data[pointer + 10:pointer + 16])
    d3 = list(struct.unpack(f'<{f3[0]}b', data[f3[1]:f3[1] + f3[0]]))
    return {'D1': d1, 'D2': d2, 'D3': d3}


def parse_c(data, pointer):
    c1, c2 = struct.unpack('<iQ', data[pointer:pointer + 12])
    return {'C1': c1, 'C2': c2}


def parse_b(data, pointer):
    b1 = parse_c(data, pointer)
    f2 = struct.unpack('<H', data[pointer + 12:pointer + 14])
    b2 = parse_d(data, f2[0])
    return {'B1': b1, 'B2': b2}


def parse_a(data, pointer):
    a1 = ''.join(map(str, struct.unpack('<6c',
                                        data[pointer:pointer + 6])))
    a1 = a1.replace('\'', '')[1::2]
    a2 = list()
    for i in range(6):
        a2.append(parse_b(data, pointer + 6 + i * 14))
    return {'A1': a1, 'A2': a2}


def main(data):
    return parse_a(data, 4)


# Testing
pprint.pprint(main(b'OLPCccphck$*m\xeb\xb5\xef\x0bz\xb2\xfa\x8a\x8b`\x00AF\x99\xbc")\xb6\xbb'
                   b'e\xd27"r\x00L`><f&\xb1\xff\xecX\xe7M\x84\x009"\xdcR\xfcl\x12\t\xdex\x03;'
                   b'\x96\x00+\x98\xf9\x89\ny\xe0\xd5\xda\xff\x01T\xa8\x00B\x11\x8cO\x94\xcaz{'
                   b'_\xb3\xed\xc9\xba\x009M\x85\xb9\xfa\x93?\xb1\x17\x0c\x80\x15\x02\x00'
                   b'^\x00\x00\x00\t$\xb3\xb7T\x1f\xce\xb4iHsH\x02\x00p\x00\x00\x00G\xcd+)\xdf{'
                   b'v\x89\xec\xd8\xecn\x02\x00\x82\x00\x00\x00&\x0f\x84\xd8v\xf7<\xeflMki'
                   b'\x02\x00\x94\x00\x00\x00S*\xdbC\xbe\xe2\x92zr\t\xf3\x9a\x02\x00'
                   b'\xa6\x00\x00\x00\xa0\x0cui\xeaC0\xbf\x02\xda\x1f[\x02\x00\xb8\x00\x00\x00'))
