# def myMessage():
#     def f01():
#         print('Привет')
#
#     def f02():
#         print('Пока')
#
#     f01()
#     f02()
#
#
# myMessage()

# Ctrl + Shift + U - изменение регистра
# Ctrl + Alt + L - быстрое форматирование кода
# Ctrl + / - комментарий
# Ctrl + D - копирование
# Ctrl + Shift + стрелки вверх/вниз
# Ctrl + W - выделение блока
# Ctrl + Shift + E
# Ctrl + F11


def say_hello(name='ПЕТР', age=24):
    if not isinstance(name, str):
        print(f'Неверный тип в name {type(name)}')
        return
    print(f'Имя: {name}, возраст: {age}')


say_hello('Иван', 34)
say_hello(age=25, name=45)
say_hello()


# def print_person(name, age, /, company):
#     print(f'Имя: {name}, возраст: {age}, компания: {company}')
#
# print_person(40, 'Денис', company='ПО "Информэнергосвязь"')


def sum1(*numbers):
    result = 0
    for n in numbers:
        result += n
    return f'Сумма = {result}'


#
#
# print(sum1(1, 3, 5, 7, 9))
# print(sum1(5, 8, 10, 2, 3, 26, 56, 4))


def primer():
    return


print(primer())
