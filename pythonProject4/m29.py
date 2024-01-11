def print_people(people):
    match people:
        case ['Tom', 'Sam', 'Bob'] | ['Tomas', 'Sam', 'Bob']:
            print('default_user')
        case ['Tom', second, _]:
            print('Second person', second)
        case [first, second, third]:
            print(f'{first}, {second}, {third}')


print_people(['Tom', 'Sam', 'Bob'])
print_people(['Tom', 'Mike', 'Bob'])
print_people(['Alice', 'Bill', 'Kate'])
print_people(['Tom', 'Sam'])


# def print_people(people):
#     match people:
#         case [first, *other]:
#             print(f'{first}, {other}')
#         # case [_, _]:
#         #     print('2 элемента')
#         # case [_, _, _]:
#         #     print(f'3 элемента')
#         case _:
#             print('Не известно')
#
#
# print_people(['Tom'])
# print_people(['Tom', 'Mike'])
# print_people(['Alice', 'Bill', 'Kate'])
# print_people(['Tom', 'Sam'])
# print_people('Tom')
#
