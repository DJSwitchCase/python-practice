def clean():
    while '$' in bad_subj:
        bad_subj.remove('$')

bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14',
            'к02 21', '1.3.py', 'В 11 4', '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12',
            'к08 24', 'к07 23', '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21',
            'к2 в3',
            'В104', 'В1013', 'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10',
            'ПитонН4 н11',
            'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']
# проверяем на буквы группы первым символом
for i in range(len(bad_subj)):
    if bad_subj[i][0] not in ['к', 'К', 'K', 'k', 'B', 'В', 'в', 'Н', 'н', 'И', 'и', 'м', 'М']:
        bad_subj[i] = '$'
clean()

# проверяем на второй символ (от 1 до 9) ф-ия отдельно, потому что так работает
for i in range(len(bad_subj)):
    if bad_subj[i][1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        bad_subj[i] = "$"
# Удаляем. Функцию делаем неколько раз, а не сразу, потому что только так работает
clean()
for i in range(len(bad_subj)):
    if len(bad_subj[i]) not in [5, 6, 4]:
        bad_subj[i]=('$')
clean()
#print(bad_subj)

for i in range(len(bad_subj)):
    if bad_subj[i][2] != ' ' and bad_subj[i][3] != ' ':
        bad_subj[i] = "$"
clean()
#print(bad_subj)
for i in range(len(bad_subj)):
    if bad_subj[i][3] in ('к', 'К', 'K', 'k', 'B', 'В', 'в', 'Н', 'н', 'И', 'и', 'м', 'М'):
        bad_subj[i] = "$"
clean()
#СЮДА!!!!!!!!!!
print(bad_subj)
