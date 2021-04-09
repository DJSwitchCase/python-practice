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
# транспонирование матрицы
def transpose_list(list_of_lists):
    for i in zip(*list_of_lists):
        print(list(i))

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
                                          'заставляет искать варианты ', 'не оставляет шанса для',
                    'повышает вероятность', 'обостряет проблему']

            set5 = ['знаний и компетенций.', 'непроверенных гипотез.',
                    'волатильных активов.', 'опасных экспериментов.',
                    'государственно-частных партнёрств.', 'цифровых следов граждан.',
                    'нежелательных последствий.', 'внезапных открытий.']
            if n == 1:  # для первого "Коллеги"
                --n
                yield set1[0]
            else:
                yield random.choice(list(set1))
            yield random.choice(list(set2))
            yield random.choice(list(set3))
            yield random.choice(list(set5))


#генератор фамилий
def nameGenerator():
    firstname = ['Данил', 'Роман', 'Лев', 'Ильдар', 'Николай', 'Семен',
             'Самир', 'Тамерлан', 'Святослав', 'Герман', 'Леонид']
    root = ['Фуц', 'Фецач', 'Шолод', 'Тачас', 'Мугод', 'Таб', 'Чер', 'Тифом', 'Гуз',
            'Наб', 'Семид', 'Баш', 'Кунар', 'Гид', 'Саб']
    suffix = ['ий', 'ли', 'як', 'ич', 'ян', 'ко', 'ин']

    yield random.choice(firstname)
    yield random.choice(root)+random.choice(suffix)
    print("\n")


# только именные аргументы
def only( * , arg1, arg2):
    print(arg1, arg2)

# array
def generate_array(dim1, dim2, dim3):
    a1 = []
    for k in range(4): #кол-во списков
        a2 = []
        for j in range(50):
            a3 = []
            for i in range(4): #кол-во элементов в списке
                a3.append(0)
            a2.append(a3)
        a1.append(a3)
    return a1

#
def generate_array2():
    # https://www.ict.social/images/1/csp/basics/3d_array.png куб
    # https://www.ict.social/python/basics/multidimensional-lists-in-python код
    cinemas = []
    for z in range(6): #кол-во сторон фигуры (6 у куба)
        cinema = []
        for y in range(4): #кол-во "столбцов" стороны куба
            column = []
            for x in range(4): #кол-во "строк" стороны куба
                column.append(0)
            cinema.append(column)
        cinemas.append(cinema)
    return cinemas
        # main
s = ['1', '1', '2', '3', '4', '4', '5']
x = [1, 7, 2, 3, 4, 5, 3, 2, 1, 1, 5, 6]
z = ["privet", "kak dela", "alo1"]
# zadanie1(s)
# zadanie2(s)
# zadanie3(s)
# zadanie4(s, '4')
# zadanie5(x)
# zadanie6(z)
#zip()
'''
s = 'abc'
t = (10, 20, 30)
print(zip(s,t))
'''
# генератор докладов
'''
generator = report_generator(1)
generator2 = report_generator(0)
print(next(generator), next(generator), next(generator), next(generator),  sep=" ")
print(next(generator2), next(generator2), next(generator2), next(generator2),  sep=" ")
'''
# для *
'''
 fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}
 print(get_multiple('lemon', 'tomtato', 'tomato', dictionary=fruits, default='unknown'))
'''

# для транспонирования
'''
a = [[0,1,2], [4,5,6], [7,8,9]]
print(*a, sep="\n")
print("\n")
transpose_list(a)
'''

# print()
'''
print(25)
sys.stdout.write(str(25) + '\n')
print(25)
'''

# именные
'''
only(arg1=1,arg2=2)
'''

# генератор фамилий
'''
for i in range(6):
    generator = nameGenerator()
    print(next(generator), next(generator))
'''
#генератор массивов
dim1 = [1,2,3]
dim2 = [4,5,6]
dim3 = [7,8,9]
#print(generate_array(dim1, dim2, dim3))
print("\n")
matrix = generate_array(dim1, dim2, dim3)
matrix[2][0] = 1
print (generate_array2())

# print(matrix)

# print(c is d) = False, потому что оператор is проверяет на то, являются ли объекты различными.
    # Для c и d выделены различные участки памяти, поэтому is выдаёт False
    # В то же время, оператор == выдаст True, потому что он проверяет значение объектов.
# a is d = True судя по всему потому, что они и являются одним объектом? Разделяют один участок памяти?


# a is c = False, потому что a и c занимают разные участки памяти. Это можно определить с помощью функции id()


