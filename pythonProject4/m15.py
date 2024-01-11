# Словари

# s1 = {'tom@mail.ru': 'Tom', 2: 'Mary', '3': 'Bob'}
#
# print(s1)
#
# user_list = (
#     ('111', 'Tom'),
#     ('222', 'Bob'),
#     ('333', 'Mary')
#      )
#
# print(user_list)
#
# user_dict = dict(user_list)
#
# print(user_dict)

# s1 = {'tom@mail.ru': 'Tom', 2: 'Mary', '3': 'Bob', '9': 'Klark'}
# # s1['3']='Mark'
# # print(s1)
# #
# # key='33'
# #
# # if key in s1:
# #     print(s1[key])
# # else:
# #     print('Error')
# print(s1)
#
# # del s1['9']
#
# print(s1.pop('9'))
# print(s1)

# s1 = {'tom@mail.ru': 'Tom', 2: 'Mary', '3': 'Bob', '9': 'Klark2'}
# s2 = {'4': 'Tom', 5: 'Mary', '6': 'Bob', '9': 'Klark'}
#
# s3 = s1.copy()
# s3.update(s2)
#
# print(s1)
# print(s3)
#

# s1 = {'tom@mail.ru': 'Tom', 2: 'Mary', '3': 'Bob', '9': 'Klark2'}
#
# for key in s1.values():
#     print(f'{key}')


users = {
    'Tom': {
        'phone': '+798765433',
        'email': 'tom@gmail.com'
    },
    'Bob': {
        'phone': '+79876548888',
        'email': 'bob@gmail.com',
        'skype': 'bob123'
    }
}

print(users)
print(users['Tom']['email'])
