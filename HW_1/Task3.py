"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
Для генерации случайного числа используйте код:

from random import
randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f'Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT} за {ATTEMPTS} попыток')
attempt = ATTEMPTS
while attempt > 0:
    x = int(input(f'У вас осталось {attempt} попыток(-ки).\nВведите число: '))
    if x == num:
        print('Поздравляем. Вы угадали число')
        attempt = -1
    else:
        if x > num:
            print('Вы ввели число больше загаданного')
        else:
            print('Вы ввели число меньше загаданного')
    attempt -= 1
if attempt == 0:
    print('Увы. Попытки кончились')

