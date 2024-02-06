"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
 Для простоты договоримся, что год может быть в диапазоне [1, 9999].
 Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
 Проверку года на високосность вынести в отдельную защищённую функцию.
 В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

from sys import argv


def _check_leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def check_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 1 < day > 31 or 1 < month > 12 or 1 < year > 9999:
        return False
    if month == 2 and (day > 28 and not _check_leap_year(year) or day > 29 and _check_leap_year(year)):
        return False
    if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        return False
    else:
        return True

date_ = argv[1:]

if __name__ == '__main__':
    date_ = argv[1]
    print(check_date(date_))