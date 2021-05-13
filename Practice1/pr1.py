# variant_23
import math


def f11(x, y, z):
    return ((75*(y**5)+x**8)/(math.log(12*(z**3))-z**8/14))\
           + math.sqrt((y**4+x**7)/(12*x**2-math.sin(z)))\
           + ((59*x**6-55*y)/(math.tan(y)+z/69))


def f12(x):
    if x < -9:
        return 75*x**5 + x**8
    if -9 <= x < 12:
        return math.log(12*x**8 - x**5/14)
    if 12 <= x < 107:
        return math.cos(math.log(x) - 95*x**5) - x**3 - 12
    if 107 <= x < 166:
        return ((math.cos(x) + 78*x**8)**3)/58 - x**5
    if x >= 166:
        return 62*x**2 - 12*x**5 + 3


def f13(n, m):

    def first_half(n):
        x = 0
        for i in range(1, n+1):
            x += 75*i**5 + i**8
        return x

    def second_half(n, m):
        x = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                x += 87*i**7 + math.fabs(i)
        return x

    return 76*first_half(n) - second_half(n, m)


def f14(n):
    if n == 0:
        return 9
    else:
        return math.sin(f14(n - 1)) + math.tan(f14(n - 1))


#проверка 1.1
#print("{:.2e}".format(zadanie1_1(69, -34, 20)))
#print("{:.2e}".format(zadanie1_1(8, 91, 39)))

#проверка 1.2
#print("{:.2e}".format(zadanie1_2(181)))
#print("{:.2e}".format(zadanie1_2(164)))

#проверка 1.3
#print("{:.2e}".format(zadanie1_3(27, 82)))
#print("{:.2e}".format(zadanie1_3(36, 66)))

#проверка 1.4
#print("{:.2e}".format(zadanie1_4(10)))
#print("{:.2e}".format(zadanie1_4(12)))