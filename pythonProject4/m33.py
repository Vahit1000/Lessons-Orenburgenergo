import random

n1 = random.random()   # 0.0 - 1.0
print(n1)

n2 = random.randint(20, 45)
print(n2)

n3 = random.randrange(10, 200, 4)
print(n3)

n4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# random.shuffle(n4)
print(n4)
r_n4 = random.choice(n4)
print(r_n4)


