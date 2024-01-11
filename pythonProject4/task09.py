# Шахматка в массив размерностью n * m. Вывести на печать. Пример:
# _ * _ * _ *
# * _ * _ * _
# _ * _ * _ *

n = 7
m = 12

ch = ['_', '*']

result = [[ch[(i + j) % 2] for i in range(m)] for j in range(n)]

for item in result:
  print(*item)
