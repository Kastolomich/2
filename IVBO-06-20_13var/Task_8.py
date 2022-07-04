def main(x):
    x = x.replace('<sect>', '')\
        .replace('</sect>', '')\
        .replace('let', '')\
        .replace('`', '')\
        .replace('[', '')\
        .replace(']', '')\
        .replace('\n', ' ')\
        .replace(' ', '')
    x_parts = x.split('.')
    x_parts.pop(-1)
    x_parts1 = [i.split('=') for i in x_parts]
    result = {}
    for i in x_parts1:
        value = i[1].split(',')
        for j in range(len(value)):
            value[j] = int(value[j])
        result[i[0].replace(',', '')] = value
    return result


# Testing
print(main('<sect> [ let `edar=[ 1119 , 1824 , 5114 ,-3892]. ], [let `uste =[ 4868, 8402].], [ let `tiat =[ -6056, 594, 6555 , -6536 ]. ], </sect>'))
