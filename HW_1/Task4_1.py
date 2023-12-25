"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
Для генерации случайного числа используйте код:

from random import
randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint
num = randint(0, 1000)
print('Угадайте число от 0 до 1000 за 10 попыток')
attempt = 10
while attempt > 0:
    x = int(input(f'У вас осталось {attempt} попыток. Введите число: '))
    if x == num:
        print('Поздравляем. Вы угадали число')
        attempt = -1
    else:
        if x > num:
            print('Вы вели число больше загаданного')
        else:
            print('Вы вели число меньше загаданного')
    attempt -= 1
if attempt == 0:
    print('Увы. Попытки кончились')

