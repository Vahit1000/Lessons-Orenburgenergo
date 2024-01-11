# Задание 1. В цикле вводить числа с клавиатуры.
# Определять простое оно, или нет с выводом сообщений.
# Предусмотреть выход из цикла.

# def smp_tst(n):
#     i = 2
#     x = n // 2 + 1
#     while (i < x) and (simple := (n % i) != 0):
#         i += 1
#     return simple
#
#
# while (a := int(input('Введите число больше 3 (0 - выход): '))) > 3:
#     print(a, 'простое' if smp_tst(a) else 'не простое')

# Задание 1. В цикле вводить числа с клавиатуры. Определять простое оно, или нет с
# выводом сообщений. Предусмотреть выход из цикла.
exitProg = False
primeNumber = 0
while exitProg == False:
    message = input("Введите число. (Для выхода введите exit): ")
    if message == "exit":
        exitProg = True
    else:
        primeNumber = 0
        number = int(message)
        for i in range(1, number + 1):
            # print(f"i = {i}")
            n = number % i
            # print(f"n = {n}")
            if n == 0:
                primeNumber += 1
        # print(f"primeNumber = {primeNumber}")
        if primeNumber > 2:
            print(f"Число {number} - не простое")
        else:
            print(f"Число {number} - простое")
