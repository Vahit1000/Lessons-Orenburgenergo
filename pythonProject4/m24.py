import csv

fileName = 'user.csv'
#
# users = [
#     ['Tom', 35],
#     ['Alice', 26],
#     ['Bob', 45]
# ]
#
# with open(fileName, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
#     user = ['Sam', 39]
#     writer.writerow(user)
#
#     file.close()
#
# # with open(fileName, 'r') as file:
# #     for ln in file:
# #         print(ln, end='')
#
# with open(fileName, 'r', newline='') as file:
#     reader = csv.reader(file)
#     for r in reader:
#         print(f'{r[0]} - {r[1]}')
#     file.close()


users = [
    {"name": 'Tom', "age": 35},
    {"name": 'Alice', "age": 28},
    {"name": 'Bob', "age": 19}
]

with open(fileName, 'w', newline='') as file:
    column = ['name', 'age']
    writer = csv.DictWriter(file, fieldnames=column)
    # запись заголовок
    writer.writeheader()
    # запись нескольких строк
    writer.writerows(users)
    # запись одной строки
    user = {"name": 'Sam', "age": 55}
    writer.writerow(user)

    file.close()


with open(fileName, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for r in reader:
        print(f'{r['name']} - {r['age']}')

