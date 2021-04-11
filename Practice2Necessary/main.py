# 2.1
def step_one(tree, x):
    if type(tree[x[1]]) is dict:
        step_three(tree, x)
    else:
        return tree[x[1]]


def step_three(tree, x):
    print (tree[x[3]])
    if type(tree[x[3]]) is dict:
        step_two(tree, x)
    else:
        return tree[x[3]]


def step_two(tree, x):
    if type(tree[x[2]]) is dict:
        step_zero(tree, x)
    else:
        return tree[x[2]]


def step_zero(tree, x):
    return tree[x[0]]


def f21(arr):
    tree = {
        'scaml': 10,
        'vhdl': 9,
        'yacc': {
            '1980': 8,
            '1983': 7,
            '2013': {
                '2012': 0,
                '1986': {
                    '1968': 1,
                    '2006': 2,
                    '1995': 3
                },
                '2018': {
                    '1968': 4,
                    '2006': 5,
                    '1995': 6
                }
            }
        }
    }
    step_one(tree, arr)

print(f21([1995, 'yacc', 1986, 2013, 'coq']))
