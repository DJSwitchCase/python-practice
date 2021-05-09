import struct
F_SIZE = 8 + 4 + 1*3 + 4 #di(BBB)f
E_SIZE = 1 + 2 + 8 + 8 + 4 + 4 + 4 #BHQdIff
D_SIZE = 4 + 2 + 4 #fhI
C_SIZE = (4 + 2) + 4 + D_SIZE + E_SIZE + 4 + 4#(IH)i??iI
B_SIZE = 1*3 + 2 #(ccc)h
A_SIZE = B_SIZE*5 + 8 + 2 + C_SIZE + 4 #!BBBBB!qh!C!I


def parse_a(offset, byte_string):
    a11 = parse_b(offset, byte_string)
    a12 = parse_b(offset + B_SIZE, byte_string)
    a13 = parse_b(offset + 2 * B_SIZE, byte_string)
    a14 = parse_b(offset + 3 * B_SIZE, byte_string)
    a15 = parse_b(offset + 4 * B_SIZE, byte_string)
    a1 = [a11, a12, a13, a14, a15]
    a_23bytes = byte_string[offset + 5*B_SIZE:offset + 5*B_SIZE + 8 + 2]
    a23_parsed = struct.unpack('>qh', a_23bytes)
    a4 = parse_c(offset+5*B_SIZE + 8 + 2, byte_string)

    a5_bytes = byte_string[offset+5*B_SIZE + 8 + 2 + C_SIZE:offset+5*B_SIZE + 8 + 2 + C_SIZE + 4]
    a5_parsed = struct.unpack('>I', a5_bytes)
    a5 = parse_f(a5_parsed[0], byte_string)
    return {'A1': list(a1),
            'A2': a23_parsed[0],
            'A3': a23_parsed[1],
            'A4': a4,
            'A5': a5}

def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>ccch', b_bytes)
    return {'B1': b_parsed[0:3],
            'B2': b_parsed[3]}


def parse_c(offset, byte_string):
    c1_bytes = byte_string[offset: offset + 4 + 2]
    c1_bytes_parsed = struct.unpack('>IH', c1_bytes)
    c1_parsed = struct.unpack('f'*c1_bytes_parsed[0], byte_string[c1_bytes_parsed[1]: c1_bytes_parsed[1] + c1_bytes_parsed[0]*4])
    c2_bytes = byte_string[offset + 4 + 2: offset + 4 + 2 + 4]
    c2_parsed = struct.unpack('>i', c2_bytes)
    c3_parsed = parse_d(offset + 4 + 2 + 4, byte_string)
    c4_parsed = parse_e(offset + 4 + 2 + 4 + D_SIZE, byte_string)
    c56_bytes = byte_string[offset + 4 + 2 + 4 + D_SIZE + E_SIZE:offset + 4 + 2 + 4 + D_SIZE + E_SIZE + 4 + 4]
    c56_parsed = struct.unpack('>iI', c56_bytes)
    return {'C1': list(c1_parsed),
            'C2': c2_parsed,
            'C3': c3_parsed,
            'C4': c4_parsed,
            'C5': c56_parsed[0],
            'C6': c56_parsed[1]}

def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>ccch', b_bytes)
    return {'B1': list(b_parsed[0:3]),
            'B2': b_parsed[3]}


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset: offset + D_SIZE]
    d_parsed = struct.unpack('>fhI', d_bytes)
    return {'D1': d_parsed[0],
            'D2': d_parsed[1],
            'D3': d_parsed[2]}


def parse_e(offset, byte_string):
    e_bytes = byte_string[offset:offset + E_SIZE]
    e_parsed = struct.unpack('>BHQdIff', e_bytes)
    return {'E1': e_parsed[0],
            'E2': e_parsed[1],
            'E3': e_parsed[2],
            'E4': e_parsed[3],
            'E5': e_parsed[4],
            'E6': e_parsed[5],
            'E7': e_parsed[6]}


def parse_f(offset, byte_string):
    f_bytes = byte_string[offset:offset + F_SIZE]
    f_parsed = struct.unpack('>diBBBf', f_bytes)
    return {'F1': f_parsed[0],
            'F2': f_parsed[1],
            'F3': f_parsed[2:5],
            'F4': f_parsed[5]}


def f31(byte_string):
    return parse_a(4, byte_string)

print(f31(((b'\xffVVGgym\x7fijag\xfc\x8dzjv$\xb6fzu\xa2\xc2ovw\x18\xbf\x95\xb7\x18:?<$'
b'\xd6,\xf9\x00\x00\x00\x02\x00f\xd3\xfc\xc7\xaf\xbc\xb4\xb8F\x8d\x00\x1d'
b'\xda;\xc9\xc0\xbc%I\xb1D\x11\xa7d\x93\xf4\xbf\xe8\xa3\xe2\xf8\x8a'
b"\xf9\xfe\xe8KD\xbb\xbe\x8a'P>\xc8\xa5\x8d\xa5a\xcb\x9a\x7f\xe0"
b'\xab\xd0\x00\x00\x00n\xbe\x9a\xc1\xa6\xbfFa"?\xbb\x8ee\x87\\\xc3\x90\xa9\xb9'
b'\xe5\xf6\xd6k<?y\x10\x19'))))