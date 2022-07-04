def main(args):
    dict4 = {'FREGE': 4, 'RUST': 5}
    dict44 = {'FREGE': 6, 'RUST': 7}
    dict3 = {1959: 9, 2019: 10}
    dict4_up = {'FREGE': 0, 'RUST': 1}
    dict44_up = {'FREGE': 2, 'RUST': 3}
    dict0 = {'STON': dict4[args[4]], 'SCAML': dict44[args[4]], 'GLYPH': 8}
    dict00 = {'STON': dict3[args[3]], 'SCAML': 11, 'GLYPH': 12}
    dict2 = {1973: dict4_up[args[4]],
             1971: dict44_up[args[4]], 2012: dict0[args[0]]}
    dict22 = {1973: dict00[args[0]], 1971: 13, 2012: 14}
    dict1 = {'LSL': dict2[args[2]], 'GAP': dict22[args[2]], 'SLIM': 15}
    return dict1[args[1]]


# Testing
print(main(['STON', 'SLIM', 2012, 2019, 'RUST']))
