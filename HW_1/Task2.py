"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

LOWER_LIMIT = 1
UPPER_LIMIT = 100_000

while True:
    num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if LOWER_LIMIT < num < UPPER_LIMIT:
        if num == 1:
            print(f'Число {num} не является простым или составным')
        elif not num % 2:
            print(f'Число {num} является составным')
        else:
            count = 0
            while count == 0:
                for i in range(3, num // 2 + 1, 2):
                    if num % i == 0:
                        count += 1
                count += 1
            if count > 1:
                print(f'Число {num} является составным')
            else:
                print(f'Число {num} является простым')
        break
    else:
        print('Введите число в заданном диапазоне')
