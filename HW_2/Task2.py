"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions."""


from fractions import Fraction
frac1 = input('Введите первую дробь(a/b): ')
frac2 = input('Введите вторую дробь(a/b): ')
x = list(map(int, frac1.split('/')))
y = list(map(int, frac2.split('/')))
numer_summ = x[0] * y[1] + x[1] * y[0]
divid_summ = x[1] * y[1]
summ_fract = [numer_summ, divid_summ]
multi_fract = [x[0] * y[0], x[1] * y[1]]
a1, b1 = summ_fract
while b1:
    a1, b1 = b1, a1 % b1
a2, b2 = multi_fract
while b2:
    a2, b2 = b2, a2 % b2
print(f'Сумма дробей {frac1} и {frac2} = {int(summ_fract[0]/a1)}/{int(summ_fract[1]/a1)}, их произведение '
      f'{int(multi_fract[0]/a2)}/{int(multi_fract[1]/a2)}')
print(f'Проверка с помощью Fraction: сумма = {Fraction(frac1) + Fraction(frac2)}, произведение = '
      f'{Fraction(frac1) * Fraction(frac2)}')