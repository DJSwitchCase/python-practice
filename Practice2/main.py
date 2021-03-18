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
     for i in s:
         print(type(i), end = ' ')


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
    pass


s = ['1', '1', '2', '3', '4', '4', '5']
x = [1, 7, 2, 3, 4, 5, 3, 2, 1, 1, 5, 6]
# zadanie1(s)
# zadanie2(s)
# zadanie3(s)
# zadanie4(s, '4')
zadanie5(x)

