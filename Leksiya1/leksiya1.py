#ЧАСТЬ 1
def part1(n):
    if (n==12):
        return 3+3+3+3
    elif (n==16):
        return 4+4+4+4
    elif (n==15):
        return 7+7+7-3-3
    elif (n==29):
        return 5+5+5+5+5+5-1

#import antigravity - пасхалка, связанная с гравитацией

#(True*2+False)*-True) = -2, потому что True = 1, а False = 0. (1*2+0)*(-1)=-2

'''
1 = 2
SyntaxError: cannot assign to literal

if
SyntaxError: invalid syntax

sum_kek
NameError: name 'sum_kek' is not defined

pr1.py
'''

#0.6+0.3==0.9 выдает False, потому что это равно 0.89999. Это происходит из-за
#особенность представления чисел в формате float (не все числа можно представить
#в 64 битах, потому что некоторые из них нельзя представить в формате с плава
#ющей точкой с основанием 2)

#ЧАСТЬ 2
'''
x = 5
1 < 5 < 10
True
x = 5
1 < (5 < 10)
False
'''
#Я думаю, что в первом случае идёт True<10, т.е. 1<10  =>True
#А во втором 1<(True), т.е. 1<1  => False


def naive_mul(x, y):
    r = x
    for i in range(0, y-1):
        x += r
    print(x)

#WORK IN PROGRESS
    
