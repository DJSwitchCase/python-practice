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

#Преобразовать элементы списка s из строковой в числовую форму.
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
   for i in s[::-1]: #выводим с шагом -1
       print(i, end=' ')


#Выдать список индексов, на которых найден элемент x в последовательности s.
def zadanie4(s, x):
    print([k for k, v in enumerate(s) if v == x]) #используем генератор


s = ['1', '1', '2', '3', '4', '4', '5']
x = [1, 1, 2, 3, 4, 5]
# zadanie1(s)
# zadanie2(s)
# zadanie3(s)
zadanie4(s, '4')
