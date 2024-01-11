# def print_data(user):
#     match user:
#         case ('Tom', 35) | ('Sam', 22):
#             print('Default user')
#         case ('Tom', age):
#             print(f'age: {age}')
#         case (name, _):
#             print(f'name: {name}')
#         case (name, age):
#             print(f'name: {name}, age: {age}')
#         # case (_, _):
#         #     print('Underfined user')


# def print_data(user):
#     match user:
#         case (name, age):
#             print(f'name: {name}, age: {age}')
#         case (name, age, company):
#             print(f'name: {name}, age: {age}, company: {company}')


# def print_data(user):
#     match user:
#         case ('Tom', 35, *rest):
#             print(f'Rest: {rest}')
#         case (name, age, *rest):
#             print(f'name: {name}, age: {age}, rest :{rest}')

def print_data(user):
    match user:
        case ('Tom', 35, *_):
            print('Default user')
        case (name, age, *_):
            print(f'name: {name}, age: {age}')


print_data(('Tom', 35))
print_data(('Tom', 25, 'Google'))
print_data(('Tom', 18, 'Google', 'C#'))
# print_data(('Tom', 28))
# print_data(('Sam', 22))
print_data(('Bob', 19, 'Microsoft', 'Java', 'Pascal', 'SQL'))
# print_data(('Bob', 19, 'Google'))

