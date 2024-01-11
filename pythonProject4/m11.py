# people = list()
# people = []
#
#
# tom = tuple()
# tom = ('Tom', 35)
# print(tom)
#
# tom = ('Tom', )
# print(tom)

# data = ['Tom', 36, 'Microsoft']
# tom = tuple(data)
# print(len(data))
# print(len(tom))

# tom = ('Tom', 36, 'Microsoft', 'Программист')
# print(tom[0])
# print(tom[2])
# print(tom[-1])

# v1, v2, v3, v4 = tom
#
# print(v1)
# print(v2)
# print(v3)
# print(v4)

# t1=tom[1:]
# print(t1)


# def get_user():
#     name = 'Tom'
#     age = 37
#     company ='Microsoft'
#     return name, age, company
#
#
# user = get_user()
# print(user)


# def print_person(*args):
#     print(f'Имя: {args[0]}, возраст: {args[1]}, место работы: {args[2]}')
#
# bob = ('Bob', 40, 'Embarcadero', 'Mehico')
# print_person(*bob)

tom = ('Tom', 36, 'Microsoft', 'Программист')
#
# for item in tom:
#     print(item)

name = 'Bob'

if name in tom:
    print('Пользователь Tom')
else:
    print('Пользователь не найден')

