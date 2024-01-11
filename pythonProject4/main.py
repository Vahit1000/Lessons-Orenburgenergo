# try:
#     with open('primer.txt', 'a', encoding='utf8') as s_file:
#         try:
#             s_file.write('Привет мир')
#             s_file.write('\nПривет параллельный мир')
#         except Exception as ex:
#             print(ex)
#         finally:
#             s_file.close()
# except Exception as e:
#     print(e)


import csv

fileName='user.csv'

users = [
    ['Tom', 38],
    ['Alice', 27],
    ['Bob', 45]
]

with open(fileName, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(users)
