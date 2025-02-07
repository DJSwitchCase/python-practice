import math
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

def task1():
    print("Задание 1.")
    myList = []
    listSum = 0
    T = True

    while T:
        x = input("Введите число: ")
        myList.append(int(x))
        listSum += myList[-1]
        if listSum == 0:
            for el in myList:
                listSum += math.pow(el, 2)
            print(listSum)
            break


def task2():
    print("Задание 2.")
    x = int(input("Введите N: "))
    T = -1
    for l in range(1, x + 1):
        for b in range(0, l):
            T += 1
            if T >= x:
                break
            print(l)


def task3():
    print("Задание 3.")
    a = np.array([[5, 10], [2, 3]])
    print(a)
    b = np.reshape(a, a.size)
    print(b)


def task4():
    print("Задание 4.")
    A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    # aList = []
    # bList = []
    # cList = []
    aSum = 0
    bSum = 0
    cSum = 0

    for i in range(len(B)):
        if B[i] == 'a':
            # aList.append(i)
            aSum += A[i]
        elif B[i] == 'b':
            # bList.append(i)
            bSum += A[i]
        elif B[i] == 'c':
            # cList.append(i)
            cSum += A[i]
    C = dict.fromkeys(B)
    C['a'] = aSum
    C['b'] = bSum
    C['c'] = cSum
    print(C)


def tasks5_11():
    print("Задания 5 и 6.")
    data = fetch_california_housing(as_frame=True)
    dataNew = pd.concat([data.data, pd.DataFrame(data.target, columns=data.target_names)], axis=1)  # зачем columns?
    pd.set_option('display.max_columns', None)
    print(dataNew)

    print("Задание 7.")
    print(dataNew.info())

    print("Задание 8.")
    print(dataNew.isna().sum()) #isna() - Detect missing values.

    print("Задание 9.")
    dataDF = pd.DataFrame(data.data) #data.data?
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    dateDFsearched = dataDF.loc[(dataDF['Population'] > 2500) & (dataDF['HouseAge'] > 50)]
    print(dateDFsearched)

    print("Задание 10.")
    #print('Max: ' + str(dataNew['MedInc'].max()) + '\n' + 'Min: ' + str(dataNew['MedInc'].min()))

    print("Задание 11.")
    print(dataDF["MedInc"].mean())
task1()
# task2()
# task3()
# task4()
# tasks5_11()
