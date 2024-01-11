# def say_hello(): print('Hello')
#
#
# def say_goodby(): print('Good bye')
#
#
# message = say_hello
# message()
# message = say_goodby
# message()

# def sum(a, b): return a + b
#
#
# def multiply(a, b): return a * b
#
# operator = sum
# print(operator(3, 8))
# operator = multiply
# print(operator(3, 8))


# def do_oper(a, b, operation):
#     result = operation(a, b)
#     print(result)


# def sum(a, b): return a + b
#
#
# def multiply(a, b): return a * b

# do_oper(3, 4, sum)
# do_oper(3, 4, multiply)


def sum(a, b): return a + b


def subtract(a, b): return a - b


def multiply(a, b): return a * b


def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply

operation = select_operation(1)
print(operation(4, 8))

operation = select_operation(2)
print(operation(4, 8))

operation = select_operation(3)
print(operation(4, 8))
