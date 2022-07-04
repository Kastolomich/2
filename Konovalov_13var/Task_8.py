def main(x):
    x = x.replace('|', '')\
        .replace('[', '')\
        .replace(']', '')\
        .replace('def', '')\
        .replace('{', '')\
        .replace('}', '')\
        .replace('\n', ' ')\
        .replace(' ', '')
    x_parts = x.split(';,')
    x_parts.pop(-1)
    x_parts1 = [i.split('=>') for i in x_parts]
    res = {}
    for i in x_parts1:
        value = i[0].split(',')
        for j in range(len(value)):
            value[j] = int(value[j])
        res[i[1]] = value
    return res


# Testing
print(main('|| [[ def { 2779 ,6346 , -4554 }=>xeus; ]], [[ def{-7476 , -9858 , -4946, -2271 } => maer_938; ]],[[ def {-6535 , 5788 , -8773 }=> maes_644;]], [[ def{ 439 , 6129 ,4844,9593} => teorer_518; ]], ||'))
