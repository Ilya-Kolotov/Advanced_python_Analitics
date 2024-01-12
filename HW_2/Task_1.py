"""Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата."""

BASE_DIV = 16
num = int(input('Введите число:'))
result_num = ''
original_num = num
x1 = [10, 11, 12, 13, 14, 15]
x2 = ['a', 'b', 'c', 'd', 'e', 'f']
dict_hex = dict(zip(x1, x2))
while num:
    rem_of_the_div = num % BASE_DIV
    if rem_of_the_div in x1:
        result_num = dict_hex[rem_of_the_div] + result_num
    else:
        result_num = str(rem_of_the_div) + result_num
    num //= 16
print(f'Число {original_num} в 16-ричной системе = {result_num}')
print(f'Проверка при помощи встроенной функции: число {original_num} в 16-ричной системе = {hex(original_num)[2:]}')