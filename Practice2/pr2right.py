# 2.1
def step_one(tree, x):
    if type(tree[x[1]]) is dict:
        return step_three(tree['yacc'], x)
    else:
        if x[1] == 'vhdl':
            return tree['vhdl']
        elif x[1] == 'scaml':
            return tree['scaml']


def step_three(tree, x):
    if type(tree[x[3]]) is dict:
        return step_two(tree[2013], x)
    elif x[3] == 1983:
        return tree[x[3]]
    elif x[3] == 1980:
        return tree[x[3]]


def step_two(tree, x):
    if type(tree[x[2]]) is dict:
        if x[2] == 1986:
            return step_zero(tree[1986], x)
        elif x[2] == 2018:
            return step_zero(tree[2018], x)
    else:
        return tree[x[2]]


def step_zero(tree, x):
    return tree[x[0]]


def f21(x):
    tree = {
        'scaml': 10,
        'vhdl': 9,
        'yacc': {
            1980: 8,
            1983: 7,
            2013: {
                2012: 0,
                1986: {
                    1968: 1,
                    2006: 2,
                    1995: 3
                },
                2018: {
                    1968: 4,
                    2006: 5,
                    1995: 6
                }
            }
        }
    }
    # a = tree['yacc']
    # b = a[2013]
    # c = b[2012]
    # print(c)
    return step_one(tree, x)
#print(f21([1995, 'yacc', 1986, 2013, 'coq']))
#print(f21([1968, 'yacc', 2018, 2013, 'coq']))
# [([1995, 'yacc', 1986, 2013, 'coq'], 3), ([2006, 'scaml', 2018, 1980, 'antlr'], 10), ([1995, 'vhdl', 2018, 1983, 'hlsl'], 9),
#  ([1968, 'yacc', 1986, 1980, 'coq'], 8), ([2006, 'yacc', 1986, 2013, 'hlsl'], 2),
#  ([1995, 'yacc', 1986, 1983, 'coq'], 7), ([2006, 'yacc', 2012, 2013, 'antlr'], 0), ([1968, 'yacc', 2018, 2013, 'coq'], 4)]

# 2.2
def f22(h):
    a = (h & 0x0000003F)
    b = (h & 0x00007FC0) << 17
    c = (h & 0x00038000) << 5
    d = (h & 0x7FFC0000) >> 12
    e = (h & 0x80000000) >> 12
    return (int(a+b+c+d+e))
#print(f22(0x15ee75ee))
#print(f22(0x05a03b2c))





# 2.3
def f23(d):
    #print(d)
    # удаление пустых строк
    for i in range(len(d)):
        d[i] = list(filter(None, d[i]))
    # добавляем столбец
    d_temp = []
    for i in d[1]:
        temp = int(i[4])
        temp = 'N' if temp == 0 else 'Y'
        i = temp
        d_temp.append(i)
    d.insert(2, d_temp)

    # преобразование
    d_temp2 = []
    for i in d[0]:
        temp = i[3:6]
        temp2 = "(" + temp + ") " + i[7:12] + i[12:].replace('-', '')
        i = temp2
        d_temp2.append(i)
    d_temp3 = []
    for i in d[1]:
        temp = i[0:2]
        temp = round(int(temp) / 100, 1)
        i = temp
        d_temp3.append(i)


    # вывод
    d.clear()

    for i in range(0, len(d_temp)):
        d.append([d_temp2[i], d_temp3[i], d_temp[i]])
    return d


d = [
    ['+7 555 767-03-31', None, '+7 418 011-71-06',
      '+7 944 488-62-89', '+7 206 206-74-37'],
    ['41%#0', None, '67%#0', '41%#1', '77%#1',]
                                                ]
d2 = [[None, '+7 897 871-94-41', '+7 193 088-86-05', '+7 335 467-74-10'],
     ['46%#1', '24%#0', '35%#0']]
#print(f23(d))
#print(f23(d2))