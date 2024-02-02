"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(15):
    print(next(fib))