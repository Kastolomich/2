def main(x):
    dict3 = {1986: 0, 2013: 1, 2020: 2}
    dict33 = {1986: 3, 2013: 4, 2020: 5}
    dict2 = {'COQ': 6, 'OPA': 7}
    dict333 = {1986: 8, 2013: 9, 2020: 10}
    dict0 = {'M': dict3[x[3]], 'FLUX': dict33[x[3]]}
    dict00 = {'M': dict2[x[2]], 'FLUX': dict333[x[3]]}
    dict1 = {'JFLEX': dict0[x[0]], 'TOML': dict00[x[0]]}
    return dict1[x[1]]
