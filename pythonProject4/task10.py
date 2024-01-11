# Написать функцию формирующую треугольник Паскаля. Второе задание - красиво напечатать.

#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
# 1 5 10 10 5 1

n = 15
p = [[1] * i for i in range(1, n + 1)]

for i in range(2, n):
    for j in range(1, i):
        p[i][j] = p[i - 1][j - 1] + p[i -1][j]

mx = len(' '.join(str(x) for x in p[-1]))

for ln in p:
    s = ' '.join(str(x) for x in ln)
    # print(s.center(mx))
    print(f'{s:^{mx}}')
