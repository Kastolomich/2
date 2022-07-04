from datetime import datetime


def main(*args):
    unzip = [*args]
    data = [x for i in unzip for x in i]
    tpls = [tuple(x) for x in data if x[0] is not None]
    dct = dict.fromkeys(tpls)
    data = [list(x) for x in dct]
    new_table = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    for i in data:
        i.pop(2)
        if len(i[0]) == 3:
            i[0] = '0.' + i[0][:-1] + '0'
        elif len(i[0]) == 2:
            i[0] = '0.0' + i[0][:-1] + '0'
        else:
            i[0] = '1.000'
        i[1] = i[1].replace('Да', 'Y')
        i[1] = i[1].replace('Нет', 'N')
        i[2] = i[2].replace('(', '').replace(')', '')
        i[2] = i[2][:10] + i[2][11:]
        date = datetime.strptime(i[3], '%d-%m-%Y')
        i[3] = datetime.strftime(date, '%d.%m.%Y')
        row1.append(i[0])
        row2.append(i[1])
        row3.append(i[2])
        row4.append(i[3])
    new_table.append(row1)
    new_table.append(row2)
    new_table.append(row3)
    new_table.append(row4)
    return new_table


# Testing
print(main(
    [['34%', 'Да', None, '(750) 442-67-15', '20-05-2003']]))

