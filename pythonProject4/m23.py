# open()
# read()
# write()
# close()

# try:
#     with open('hello.txt', 'w') as myfile:
#         try:
#             myfile.write('Ехал Ваня на окне,\n')
#             myfile.write('Вел старушку на ремне.\n')
#             myfile.write('А собачка, в это время,\n')
#             myfile.write('Мыла фикус на коне.\n')
#         except Exception as e:
#             print(e)
#         finally:
#             myfile.close()
# except Exception as ex:
#     print(ex)

# read()
# readline()
# readlines()


# try:
#     with open('hello.txt', 'r') as myfile:
#         try:
#             cont = myfile.readlines()
#             print(cont[0])
#             print(cont[1])
#             # print(myfile.read())
#             # for line in myfile.readlines():
#             #     print(line, end='')
#
#         except Exception as e:
#             print(e)
#         finally:
#             myfile.close()
# except Exception as ex:
#     print(ex)


fileName = 'mess.txt'

messages = list()

for i in range(4):
    message = input('Введите строку ' + str(i + 1) + ': ')
    messages.append(message + '\n')

# запись в файл
with open(fileName, 'w') as file:
    for m in messages:
        file.write(m)
    file.close()

# чтение файла
with open(fileName, 'r') as file:
    for m in file:
        print(m, end='')



