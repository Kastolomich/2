def main(x):
    x = x.replace('|', '')\
        .replace('auto', '')\
        .replace('#', '')\
        .replace('`', '')\
        .replace('{', '')\
        .replace('}', '')\
        .replace('.', '')\
        .replace('\n', '')\
        .replace(' ', '')
    x_parts = x.split(',')
    x_parts.pop(-1)
    x_parts1 = [i.split('==>') for i in x_parts]
    result = {}
    for i in x_parts1:
        key = i[1]
        value = int(i[0])
        result[key] = value
    return result


# Testing
print(main('{ || auto#-7518 ==> `tege.||, || auto #4889 ==>`biso_335. ||, || auto #2918 ==> `gelabi. ||, }'))

