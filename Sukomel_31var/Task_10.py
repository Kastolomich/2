from datetime import datetime
import re


def main(*args):
    unzip = [*args]
    data = [x for i in unzip for x in i]
    tpls = [tuple(x) for x in data if x[2] is not None]
    dct = dict.fromkeys(tpls)
    data = [list(x) for x in dct]
    new_table = []
    for i in data:
        i.pop(0)
        i.pop(0)
        split = i[0].split('|')
        i[0] = re.sub(r'.*@', '', split[0])
        date = datetime.strptime(i[1], '%d/%m/%y')
        i[1] = datetime.strftime(date, '%d-%m-%y')
        if i[2] == 'Не выполнено':
            i[2] = 'Нет'
        else:
            i[2] = 'Да'
        i.append(split[1][6:].replace('-', ''))
        row = []
        row.append(i[0])
        row.append(i[1])
        row.append(i[2])
        row.append(i[3])
        new_table.append(row)
    return new_table


# Testing
print(main(
    [[None, None, 'danila24@rambler.ru|(519) 482-57-13', '05/11/00', 'Не выполнено'], [None, None, None, None, None],
     [None, None, 'rirskij89@yahoo.com|(781) 080-45-54', '04/10/02', 'Выполнено'],
     [None, None, 'rirskij89@yahoo.com|(781) 080-45-54', '04/10/02', 'Выполнено'],
     [None, None, 'rirskij89@yahoo.com|(781) 080-45-54', '04/10/02', 'Выполнено'],
     [None, None, 'artemij91@yahoo.com|(729) 241-02-80', '07/08/04', 'Не выполнено'],
     [None, None, 'nikolaj84@yandex.ru|(155) 635-54-35', '16/07/01', 'Выполнено']]))
