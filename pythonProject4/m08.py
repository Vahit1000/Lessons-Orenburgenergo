# name = 'Ольга'
#
# def s1():
#     global name
#     name = 'Иван'
#     print(name)
#
# def s2():
#     name = 'Петр'
#     print(name)
#
# s1()
# s2()
#
# print(name)


# def outer():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n = 25
#         print(n)
#
#     inner()
#     print(n)
#
#
# outer()

# def outer(): # внешняя функция
#     n = 5    # локальная переменная
#
#     def inner():    # локальная функция
#         nonlocal n
#         n += 1
#         print(n)
#
#     return inner
#
# fn = outer()
#
# fn()
# fn()
# fn()
# fn()


def multiply(n): return lambda m: n * m


# def inner(m): return n * m
# return inner

fn = multiply(5)
print(fn(5))
print(fn(6))
print(fn(7))
