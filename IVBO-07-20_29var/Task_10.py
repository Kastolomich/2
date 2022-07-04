from datetime import datetime
import re


def main(*args):
    unzip = [*args]
    data = [x for i in unzip for x in i]
    tpls = [tuple(x) for x in data if x[0] is not None]
    data = [list(x) for x in tpls]
    new_table = []
    for i in data:
        i.remove(None)
        i.pop(-1)
        i[0] = re.sub(r'.*@', '', i[0])
        if i[1] == 'N':
            i[1] = 'Не выполнено'
        elif i[1] == 'Y':
            i[1] = 'Выполнено'
        date = datetime.strptime(i[2], '%d.%m.%y')
        i[2] = date.strftime('%y.%m.%d')
        row = []
        row.append(i[0])
        row.append(i[1])
        row.append(i[2])
        new_table.append(row)
    return new_table


# Testing
print(main(
    [['vigskij96@rambler.ru', None, 'N', '01.07.04', 'vigskij96@rambler.ru']]))
