def main(x):
    x = x.replace('<:', '')\
        .replace('store', '')\
        .replace('\'', '')\
        .replace(':>', '')\
        .replace('\n', ' ')\
        .replace(' ', '')
    x_parts = x.split(';')
    x_parts.pop(-1)
    x_parts1 = [i.split('|>') for i in x_parts]
    result = {}
    for i in x_parts1:
        result[i[1]] = i[0]
    return result


# Testing
print(main('<:store zaan |> \'vediri_987\'; store lequ |> \'maedes_230\'; store laxe |>\'xecean_736\';:> '))
