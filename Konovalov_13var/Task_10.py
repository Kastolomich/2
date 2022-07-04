from datetime import datetime


def main(*args):
    unzip = [*args]
    data = [x for i in unzip for x in i]
    tpls = [tuple(x) for x in data if x[0]]
    dct = dict.fromkeys(tpls)
    data = [list(x) for x in dct]
    new_table = []
    for i in data:
        i.pop(3)
        i[0] = '(' + i[0][0:3] + ') ' + i[0][4:10] + '-' + i[0][10:]
        split = i[1].split(' ')
        i[1] = split[0]
        i[2] = str(round(float(i[2]), 3))
        if len(i[2]) == 4:
            i[2] += '0'
        date = datetime.strptime(i[3], '%d.%m.%Y')
        i[3] = datetime.strftime(date, '%d-%m-%Y')
        row = []
        row.append(i[0])
        row.append(i[1])
        row.append(i[2])
        row.append(i[3])
        new_table.append(row)
    return new_table


# Testing
print(main(
    [['766-034-1423', 'Duzev S.U.', '0.9601', 'Duzev S.U.', '01.03.2000']]))

