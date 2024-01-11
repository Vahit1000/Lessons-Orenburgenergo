# m1 = 'Hello World'
# m2 = "Error message"
#
# print(m1)
# print(m2)

'''
Это комментарий
Описание
'''

# text = '''Ехал Ваня на коне
# \tВел собачку на \'ремне\'.
# А старушка, в это время\\,
# \tМыла \"фикус\" на окне.
# '''
#
# print(text)

# path = 'C:\\python\\name.txt'
# print(path)


# username = 'Tom'
# age = 45
# user = f'name: {username}, age: {age}'
# print(user)
# #
# # # print(user[-4])
# #
# # for s in user:
# #     print(s)
#
# print(f'>{user[2:11:2]}<')
# print(f'>{user[-3:8:-1]}<')

# name = 'Tom'
# surname = 'Smith'
# age = 45
# fullname = name + ' ' + surname + ', age = '+str(age)
#
# print(fullname)

# h = 'хи'
# print(h * 9)


# s1 = '1a'
# s2 = 'aa'
# s3 = 'Aa'
#
# print(s1 > s2)
# print(s2 > s3)

# name = 'Tom'
# surname = 'Smith'
#
# print(name.lower(), surname.upper())
# print(ord(name[0]))
# print(len(surname))


text = '''Ехал Ваня на коне
\tВел собачку на \'ремне\'.
А старушка, в это время\\,
\tМыла \"фикус\" на окне.
'''

if 'ремень' in text:
    print('Ok')
else:
    print('None')
