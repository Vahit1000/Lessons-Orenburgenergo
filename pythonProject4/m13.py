# people = ['Tom', 'Bob', 'Alice', 'Tom']
# users = set(people)
#
# users.add('Ted')
#
# print(users)
# # print(len(users))
#
# users.remove('Bob')
#
# print(users)
#
# # st = users.copy()
# #
# # print(st)
#
# users2 = {'Bob', 'Kate', 'Sam'}
#
# users3 = users.union(users2)
#
# print(users3)
# # users.clear()
# #
# # print(users)

# users = {'Tom', 'Alice', 'Bob'}
# users2 = {'Bob', 'Kate', 'Sam'}

# users3 = users.intersection(users2)
# print(users3)
#
# print(users & users2)
#
# users.intersection_update(users2)
# print(users)


# users = {'Tom', 'Alice', 'Bob'}
# users2 = {'Bob', 'Kate', 'Sam'}
#
# # users3 = users2.difference(users)
# #
# # print(users3)
#
# users3 = users.symmetric_difference(users2)
# print(users3)
#
# print(users ^ users2)

# users = {'Tom', 'Alice', 'Bob'}
# users2 = {'Sam', 'Tom', 'Bob', 'Greg', 'Alice'}
#
# print(users.issubset(users2))
# print(users2.issuperset(users))


users = frozenset({'Tom', 'Alice', 'Bob'})

