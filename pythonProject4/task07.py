# Задание 7
# Удалить все символы из строки указанного символа. Оформить в виде функции. Пример
# s = 'иванов:иван:иванович'
# ch = ':'

def symb(s: str, ch: str):
    '''
    Это описание функции
    :param s: Первый параметр
    :param ch: Второй параметр
    :return: Возвращаемое значение
    '''
    res = ''
    if isinstance(s, str) and isinstance(ch, str):
        if ch in s:
            res = s.replace(ch, '')
        else:
            res = f'"{ch}" - отсутствует в строке'
    else:
        res = 'Параметры должны быть строками'
    return res


s = 'иванов:иван:иванович:петров:павел:петрович:!!!'
ch = ':'

print(symb(s, ch))

