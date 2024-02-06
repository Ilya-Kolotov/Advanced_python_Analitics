"""
Напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""


def is_attack(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    return False


def input_coordinates(count_queens: int):
    coordinates_queens = []
    while count_queens:
        coor_queen = list(map(int, (input("Введите координаты от 1 до 8: ").split())))
        if coor_queen not in coordinates_queens and 0 < coor_queen[0] < 9 and 0 < coor_queen[1] < 9:
            coordinates_queens.append(coor_queen)
            count_queens -= 1
        elif coor_queen in coordinates_queens:
            print('Такие координаты уже есть')
            continue
        else:
            print('Введены не корректные координаты')
            continue
    return coordinates_queens


def check_attack(coor_queens: list):
    for i in range(len(coor_queens)):
        for j in range(i+1, len(coor_queens)):
            x1, y1 = coordinates_queens[i]
            x2, y2 = coordinates_queens[j]
            if is_attack(x1, y1, x2, y2):
                return False
    return True


if __name__ == '__main__':
    n = 8
    coordinates_queens = input_coordinates(n)
    if check_attack(coordinates_queens):
        print('Ферзи не бьют друг друга')
    else:
        print('Ферзи бьют друг друга')