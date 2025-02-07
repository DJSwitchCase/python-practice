# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def zadanie2(triangleSide, triangleHeight, rectangleSide1, rectangleSide2, circleRadius):
    triangleArea = triangleSide * triangleHeight * 0.5
    rectangleArea = rectangleSide1 * rectangleSide2
    circleArea = circleRadius ** 2 * math.pi
    dictionary = {'Площадь треугольника': triangleArea, 'площадь прямоугольника': rectangleArea,
                  'Площадь круга': circleArea}
    return ("Задание 2. Словарь: " + str(dictionary))


def zadanie3(number1, number2):
    return "Задание 3. Арифметические операции: " + str((abs(number1 + number2 - number1) / number1) ** 2 // 2)


# Press the green button in the gutter to run the script.
def zadanie4(a, b, c):
    if (a + b <= c):
        return "Некорректный треугольник: сумма любых двух сторон должна быть больше третьей"
    if (a + c <= b):
        return "Некорректный треугольник: сумма любых двух сторон должна быть больше третьей"
    if (b + c <= a):
        return "Некорректный треугольник: сумма любых двух сторон должна быть больше третьей"
    p = (a + b + c) / 2
    perimetrPoGeronu = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return "Задание 4. Площадь треугольника по Герону: " + str(perimetrPoGeronu)


print(zadanie2(5, 4, 3, 2, 6))
print(zadanie3(5, 10))
print(zadanie4(4, 15, 10))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
