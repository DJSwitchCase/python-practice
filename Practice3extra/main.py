import traceback
# Привести примеры кода, которые соответствуют следующим нарушениям PEP 8:
# 1. whitespace before '('.
# 2. missing whitespace around operator.
# 3. missing whitespace after ','.
# 4. unexpected spaces around keyword / parameter equals.
# 5. expected 2 blank lines, found 1.
# 6. multiple statements on one line (colon).
# 7. multiple statements on one line (semicolon).
# 8. comparison to None should be 'if cond is None:'.
# 9. comparison to True should be 'if cond is True:' or 'if cond:'.

# 1.

def sample ():
    pass

# 2.
a=5

# 3.
a,b = 4, 3

# 4.
def sample2(a = b):
    pass

# 5.
pass

# 6.
a = 3
if a > 5: a = 10

# 7.
a = 1; b = 5

# 8.
if a == None:
    pass

# 9.
if a == True:
    pass

# Неконтролируемый импорт с помощью *, как известно, в Питоне не поощряется.
# Попробуйте сделать его контролируемым со стороны модуля.
# Чтобы использование звездочки приводило
# к импорту пользователю только определенного круга имен вашего модуля.
from forimport import *
a1()
a2()
#a3()  # не видит

# Создать учебный пакет, состоящий из нескольких модулей и JSON-файла.
# Получить дистрибутив, готовый для установки с помощью pip. Проверить результат установки в виртуальном окружении.
'Создаём __init__.py файл, делая директорию пакетом, '
'настраиваем setup.py, собираем пакет через ' \
'"python myPackage/setup.py sdist" Создаются dist/myPackageSetup-0.0.1.tar.gz и. myPackageSetup.egg-info'
'Устанавливаем пакет с помощью "pip install Build/dist/myPackageSetup-0.0.1.tar.gz"'

#Написать функцию, которая добавляет информацию о возникшем исключении (класс, сообщение, трассировка) в лог-файл.
# Функция не должна обрабатывать исключения.
# На вход функции, которую необходимо разработать, поступает ссылка на выполняемую пользовательскую функцию:
def function():
    try:
        x = 1/0
        return x
    except Exception as e:
        exc = e
        tb_str = traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
    return tb_str


def run_with_log(func):
    f = open('logfile.txt', 'w')
    f.write(str(func))
    f.close()

run_with_log(function())