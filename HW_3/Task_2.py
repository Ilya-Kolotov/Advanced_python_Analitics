"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""


text = 'В статью большой текстовой, строке подсчитать количество встречаемых слов и вернуть 10 самых частых.\
        Не учитывать знаки препинания препинания и регистр символов документации[83] документации[83].\
        За основу возьмите любую любую любую статью ,статью, из википедии википедии строке строке или из документации к языку языку языку языку.'

punct = ',.!?:;{}[]123456789'
text_collection = text.lower().split()
i = 0
dict_collection = {}
while i < len(text_collection):
    if text_collection[i].isdigit() or len(text_collection[i]) == 1:
        text_collection.pop(i)
    else:
        text_collection[i] = text_collection[i].strip(punct)
    i += 1
for i in range(len(text_collection)):
    dict_collection[text_collection[i]] = text_collection.count(text_collection[i])
sort_dict = sorted(dict_collection.items(), key=lambda item: item[1], reverse=True)
result = []
for i in sort_dict:
    result.append(i[0])
    if len(result) == 10:
        break
print(f'Самые часто встречаемые слова -', *result)