"""
Игра с компьютером
"""

from random import randint
num = int(input('Загадайте число от 0 до 1000: '))
attempt = 0
MIN = 0
MAX = 1000
while attempt >= 0:
    turn = randint(MIN, MAX)
    if turn == num:
        print(f'Поздравляем. Вы угадали число за {attempt} попыток')
        attempt = -1
    else:
        if turn > num:
            print(f'Вы вели число {turn}, оно больше загаданного')
            MAX = turn - 1
        else:
            print(f'Вы вели число {turn}, оно меньше загаданного')
            MIN = turn + 1
        attempt += 1