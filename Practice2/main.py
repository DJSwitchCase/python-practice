import numpy as np #
import random
import sys
#ЛК
'''
help (max)
print ('privet', 'kakdela', 'etonoviy', sep='_')
print ('kadlelac', end='!\n')
print ('yoooo')

alpha = range(ord('А'), ord('Я') + 1)

beta = ''
beta.join([chr(c) for c in alpha])

firms = {'Yandex', 'Yandex', 'JetBrains', 'MCST'}
set(['Yandex', 'JetBrains', 'MCST']) # еще один вариант определения множества
firms.add('Kaspersky')
firms.remove('JetBrains')
print(firms, 'MCST' in firms, {x for x in firms if 'a' in x})
y = 5

def f(x):
    global y
    y += 5
    print(x)

f(y)
print(y)
'''

# Преобразовать элементы списка s из строковой в числовую форму.
def zadanie1(s):
     for i in s:
         int(i)
         print(i, end=' ')
     #for i in s:
        #print(type(i), end = ' ')


# Подсчитать количество различных элементов в последовательности s.
def zadanie2(s):
    print(len(set(s))) #превращаем в набор (удаляет одинаковые элементы), потом смотрим длину


# Обратить последовательность s без использования функций.
def zadanie3(s):
   for i in s[::-1]:    # выводим с шагом -1
       print(i, end=' ')


# Выдать список индексов, на которых найден элемент x в последовательности s.
def zadanie4(s, x):
    print([k for k, v in enumerate(s) if v == x])   # используем генератор


# Сложить элементы списка x с четными индексами
def zadanie5(x):
    count = 0
    for i in range(len(x)):
        if i % 2 == 0:
            count += x[i]
    print(count)


# Найти строку максимальной длины в списке строк s.
def zadanie6(x):
    print(max(len(i) for i in x))


# Пример работы *
def get_multiple(*keys, dictionary, default=None):
    return [
        dictionary.get(key, default)
        for key in keys
    ]


# изучение работы zip()
def zipp():
    s = 'abc'
    t = (10, 20, 30)
    print(zip(s, t))


# генератор докладов
def report_generator(n):
    set1 = ['Коллеги,', 'В тоже время,', 'Однако,', 'Тем не менее', 'Следовательно,', 'Соответственно,',
            'Вместе с тем', 'С другой стороны,']

    set2 = ['парадигма цифровой экономики', 'контекст цифровой трансформации',
            'диджитализация бизнес-процессов',
            'прагматичный подход к цифровым платформам',
            'совокупность сквозных технологий',
            'программа прорывных исследований',
            'ускорение блокчейн-транзакций',
            'экспоненциальный рост Big Data']

    set3 = ['открывает новые возможности для', 'выдвигает новые требования',
            'несёт в себе риски', 'расширяет горизонты'
            'заставляет искать варианты ', 'не оставляет шанса для' ,
            'повышает вероятность', 'обостряет проблему']

    set5 = ['знаний и компетенций.', 'непроверенных гипотез.',
            'волатильных активов.', 'опасных экспериментов.',
            'государственно-частных партнёрств.', 'цифровых следов граждан.',
            'нежелательных последствий.', 'внезапных открытий.']
    if n == 1: # для первого "Коллеги"
        --n
        yield set1[0]
    else:
        yield random.choice(list(set1))
    yield random.choice(list(set2))
    yield random.choice(list(set3))
    yield random.choice(list(set5))


s = ['1', '1', '2', '3', '4', '4', '5']
x = [1, 7, 2, 3, 4, 5, 3, 2, 1, 1, 5, 6]
z = ["privet", "kak dela", "alo1"]
# zadanie1(s)
# zadanie2(s)
# zadanie3(s)
# zadanie4(s, '4')
# zadanie5(x)
# zadanie6(z)
# zipp()
# для get_multiple()
'''
fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}
print(get_multiple('lemon', 'tomtato', 'tomato', dictionary=fruits, default='unknown'))
'''
# transpose()
s1 = ()
a = [[0, 1, 2], [4, 5, 6]]
a1 = [0, 1, 2]
a2 = [4, 5, 6]
# print(list(zip(a1, a2)))
# a = np.array([[0, 1, 2], [4, 5, 6]])
# print(a1, a2, sep="\n")
# print(list(zip(a*)))

# генератор докладов
'''
generator = report_generator(1)
generator2 = report_generator(0)
print(next(generator), next(generator), next(generator), next(generator),  sep=" ")
print(next(generator2), next(generator2), next(generator2), next(generator2),  sep=" ")
'''

# print()
print(25)
sys.stdout.write(str(25) + '\n')
print(25)
