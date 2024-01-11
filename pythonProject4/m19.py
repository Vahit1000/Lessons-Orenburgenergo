# isalpha()
# p ='iuyiu'
# print(p.isalpha())

# islower()
# p ='Iuyiu'
# print(p.islower())

# isupper()

# isdigit()
# p ='1234'
# print(p.isdigit())

# isnumeric()
# p ='1234.8'
# print(p.isnumeric())

# startswith()
# p ='Tom, Mary, Alice'
# print(p.startswith('Mary'))

# endswith()
# p ='Tom, Mary, Alice'
# print(p.endswith('Alice'))

# title()
# text = '''Ехал Ваня на коне
# Вел собачку на ремне.
# А старушка, в это время,
# Мыла фикус на окне.
# '''
# print(text)
# # print(text.title())
#
# # capitalize()
# print(text.lower().capitalize())


#lstrip()
#rstrip()
#strip()

# p = '  Это проверка удаления  '
#
# print(f'>{p}<')
# print(f'>{p.lstrip()}<')
# print(f'>{p.rstrip()}<')
# print(f'>{p.strip()}<')

# ljust()

# p = 'Это проверка удаления'
# print(f'>{p.ljust(30)}<')
# print(f'>{p.rjust(30)}<')
# print(f'>{p.center(30)}<')


# find()

# text = '''Ехал Ваня на коне
# Вел собачку на ремне.
# А старушка, в это время,
# Мыла фикус на окне.
# '''
# # print(text.find('на', 11, 32))
#
# # replace()
#
# print(text.replace('Ваня', 'Петя'))

#split()

# t = 'Свалился, но ничего, не испугался и плывет тихонько, а потом нырнул и тотчас достиг морского дна.'
# print(t.split(' '))

#partition
# print(t.partition(' '))


# t = 'Свалился, но ничего, не испугался и плывет тихонько, а потом нырнул и тотчас достиг морского дна.'
# m = t.split(' ')
# s = '|'.join(m)
# print(s)


# format()

# info = 'Name: {name}, Age: {age}'.format(name='Bob', age=23)
# print(info)

# info = 'Name: {0}, Age: {1}'.format('Bob', 23)
# print(info)

# w = 'Hello {:s}'
# name = 'Tom'
# ff = w.format(name)
# print(ff)
#
# s = '{:d} символов'
# t = s.format(5)
# print(t)

# n=5000
# s = f'{n:,d} символов'
# print(s)

# n = 23.567019783
#
# print(f'{n:.2f}')
# print(f'{n:.3f}')
# print(f'{n:.4f}')
# print('{:,.2f}'.format(15500001.3490973))
#
# n1 = 23.7667468
# print(f'{n1:10.2f}')
# n2 = 23
# print(f'{n2:10d}')

# p = 0.126456
# print(f'{p:%}')
# print(f'{p:.0%}')
# print(f'{p:.2%}')


# n = 123456.8764534
# print(f'{n:.2e}')










