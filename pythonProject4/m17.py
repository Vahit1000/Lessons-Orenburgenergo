# def f1(*args):
#     for arg in args:
#         print(arg)
#     print(len(args))
#
# def f2(**kwargs):
#     pass
#
# f1('Python', 'C++', 'Java')
#
#
# def summ(*args):
#     result=0
#     for arg in args:
#         result += arg
#     return  result
#
# print(summ(1, 2, 3))
# print(summ(1, 2, 3, 4, 5))
# print(summ(1, 2, 3, 6, 7))
# print(summ(1, 2, 3, 8, 9, 12, 45))


# def fun(**kwargs):
#     for key in kwargs:
#         print(f'{key} = {kwargs[key]}')
#
#
# fun(name='Tom', age=34, company='Google')


# def summ(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# name = (1, 2, 3, 4, 5)
#
# print(summ(*name))

# def peint_person(name, age, company):
#     print(f'name={name}, age={age}, company={company}')
#
# person = {'name': 'Tom', 'age': 45, 'company': 'Google'}
#
# peint_person(**person)


def s(n1, n2, *args):
    r = n1 +n2
    for n in args:
        r += n
    return r

print(s(1, 2))
print(s(1, 2, 3))
print(s(1, 2, 3, 4, 5))
print(s(1, 2, 3, 7, 8, 9))







