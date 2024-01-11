try:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    print('Результат деления:', number1 / number2)
except (ValueError, ZeroDivisionError) as e:
    print(f'Ошибка преобразования - {e}')
# except ZeroDivisionError as e2:
#     print(f'Деление на ноль - {e2}')
finally:
    print('Инструкции блока finally')
print('Программа завершила работу!')


# try:
#     Инструкция
# except:
#     Инструкиця





