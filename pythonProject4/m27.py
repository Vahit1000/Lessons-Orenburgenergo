# def print_hello(lang):
#     match lang:
#         case 'russian':
#             print('Привет')
#             print('Пока')
#         case 'english' | 'american english' | 'british english':
#             print('Hello')
#         case 'german':
#             print('Hallo')
#         case _:
#             print('Underfined')
#
# print_hello('russian')
# print_hello('english')
# print_hello('german')
# print_hello('american english')


def operation(a, b, code):
    match code:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b
        case _:
            return 0

print(operation(2, 5, 1))
print(operation(2, 5, 2))
print(operation(2, 5, 3))
print(operation(2, 5, 4))
print(operation(2, 5, 5))

