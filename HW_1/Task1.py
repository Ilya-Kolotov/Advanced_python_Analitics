"""
Вывести калькулятор как в тетради
"""

for i in range(1, 11):
    for j in range(2, 6):
        multi = i * j
        print(f'{j} x {i:2d} = {multi:2d} ', end='\t')
    print()
print()
for i in range(1, 11):
    for j in range(6, 10):
        multi = i * j
        print(f'{j} x {i:2d} = {multi:2d} ', end='\t')
    print()
