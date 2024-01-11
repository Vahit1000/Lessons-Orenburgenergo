# def select(intput_func):
#     def output_func():
#         print('************************************')
#         intput_func()
#         print('************************************')
#
#     return output_func
#
# @select
# def hello():
#     print('Здравствуй мир')
#
# hello()


# def check(input_func):
#     def output_func(*args):
#         n = args[0]
#         a = args[1]
#         if a < 0: a = 1
#         input_func(n, a)
#
#     return output_func
#
#
# @check
# def print_person(name, age):
#     print(f'Имя: {name}, возраст: {age}')
#
#
# print_person('Tom', 45)
# print_person('Alice', -5)


def check(input_func):
    def output_func(*args):
        result = input_func(*args)
        if result < 0: result = 0
        return result

    return output_func


@check
def sum_numb(a, b):
    return a + b


r1 = sum_numb(10, 20)
print(r1)
r2 = sum_numb(10, -20)
print(r2)
