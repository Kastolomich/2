def main(x):
    dict0 = {'GLSL': 2, 'RDOC': 3, 'TERRA': 4}
    dict00 = {'GLSL': 5, 'RDOC': 6, 'TERRA': 7}
    dict1 = {1978: 8, 2001: 9}
    dict2 = {'OPA': 0, 'ARC': 1, 'JFLEX': dict0[x[0]]}
    dict22 = {'OPA': dict00[x[0]], 'ARC': dict1[x[1]], 'JFLEX': 10}
    dict4 = {'MQL4': dict2[x[2]], 'BISON': dict22[x[2]]}
    dict3 = {1960: dict4[x[4]], 1969: 11}
    return dict3[x[3]]
