# message = lambda: print('Hello')
#
# message()


# def message():
#     print('Hello')

# square = lambda n: n * n
#
# print(square(2))
# print(square(4))
# print(square(8))

# sum1 = lambda a, b: a + b
#
# print(sum1(6, 9))


def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation = select_operation(1)
print(operation(4, 8))

operation = select_operation(2)
print(operation(4, 8))

operation = select_operation(3)
print(operation(4, 8))


