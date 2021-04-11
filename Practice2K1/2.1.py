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
    if x[3] == 1983:
        return tree[x[3]]
    if x[3] == 1980:
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
            'yay': 8,
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
