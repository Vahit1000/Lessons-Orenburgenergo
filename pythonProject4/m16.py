# x, y = (1, 2)
#
# print(x)
# print(y)

# name, age, company = ['Tom', 34, 'Google']
# print(name)
# print(age)
# print(company)

# d = {'red': 'красный', 'blue': 'синий', 'green': 'зеленый'}
# r, b, g = d
# print(r)
# print(b)
# print(g)

# people = [
#     ('Tom', 38, 'Google'),
#     ('Bob', 45, 'Microsoft'),
#     ('Mary', 25, 'Apple')
# ]
#
# for name, age, company in people:
#     print(f'{name}, {age}, {company}')


# poeple = ['Tom', 'Alice', 'Mary']
# for index, name in enumerate(poeple):
#     print(f'{index}, {name}')


# people = [
#     ('Tom', 38, 'Google'),
#     ('Bob', 45, 'Microsoft'),
#     ('Mary', 25, 'Apple')
# ]
#
# for name, _, company in people:
#     print(f'{name}, {company}')


# n1 = 1
# n2 = 2
# n3 = 3
# *numbers, = n1, n2, n3
# print(tuple(numbers))

# n0, *n1, n2 = [1, 2, 3, 4, 5]
# print(n0)
# print(n1)
# print(n2)
# nums1 = [1, 2, 3]
# nums2 = (4, 5, 6)
# nums3 =[*nums1, *nums2]
# print(nums3)


d1 = {'red': 'красный', 'blue': 'синий', 'green': 'зеленый'}
d2 = {'green': 'зеленый', 'white': 'белый'}
d3 = {**d1, **d2}

print(d3)



