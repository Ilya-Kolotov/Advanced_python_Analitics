"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

lst = [1,2,2,3,3,5,5,6,7,5,2,7,9]
set_elem = set(lst)
list_of_duplicates = []
for elem in set_elem:
    if lst.count(elem) > 1:
        list_of_duplicates.append(elem)
print(list_of_duplicates)