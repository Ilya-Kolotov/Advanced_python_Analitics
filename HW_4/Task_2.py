"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def func_dict(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            new_dict[str(value)] = key
        else:
            new_dict[value] = key
    return new_dict


new_dict = func_dict(stroka1="Hello", int=2, stroka2="123", list=[1, 2, 3, 4, 5])
print(new_dict)