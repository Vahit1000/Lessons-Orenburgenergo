# Задание 8
# Все слова в строке длиннее 5 символов развернуть и вывести результирующую строку
# Пример
# Свалился, но ничего, не испугался и плывет тихонько, а потом нырнул и тотчас достиг морского дна.

c = 'Свалился, но ничего, не испугался и плывет тихонько, а потом нырнул и тотчас достиг морского дна.'

n = 5

result = ' '.join((x[::-1] if len(x) > n else x) for x in c.split())
print(result)


