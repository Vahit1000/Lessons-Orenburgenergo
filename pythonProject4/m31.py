# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# def enter(person):
#     match person:
#         case Person(name=name, age=age) if age < 18:
#             print(f'{name} - доступ запрещен!')
#         case Person(name=name):
#             print(f'{name} - добро пожаловать!')
#
#
# enter(Person('Tom', 34))
# enter(Person('Alice', 17))

# def check_data(data):
#     match data:
#         case name, age if name == 'admin' or age not in range(1, 101):
#             print('Некорректное значение')
#         case name, age:
#             print(f'{name}, {age}')
#
#
# t1 = ('adm', -45)
# t2 = ('Tom', 23)
#
# check_data(t1)
# check_data(t2)


# def print_person(person):
#     match person:
#         case ('Tom' | 'Tomas' | 'Tommy' as name, 37 | 38 as age):
#             print(f'{name}, {age}')
#         case _:
#             print('?????')
#
# print_person(('Tom', 37))
# print_person(('Tomas', 38))
# print_person(('Tommy',39))



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def print_family(family):
    match family:
        case (Person() as husband, Person() as wife):
            print(f'Муж: {husband.name}, {husband.age}')
            print(f'Жена: {wife.name}, {wife.age}')
        case _:
            print('Undefined')

print_family((Person('Tom', 23), Person('Alice', 20)))

