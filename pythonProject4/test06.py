a = '''Введите номер задания
    (6 - вывести таблицу умножения
    7 - сформировать матрицу из таблицы умножения
    8 - улалить все указанные символы из строки) 
    9 - переворачиваем слова из 5 символов
    10 - проверка на полиндром:'''

oper = input(a)

if oper == '6':
    n = 10
    for i in range(n):
        i += 1
        for j in range(n):
            j += 1
            print(i * j, end='\t')
        print('\t')

if oper == '7':
    n = 11
    mass = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mass[i][j] = j * i
    for i in range(1, len(mass)):
        for i2 in range(1, len(mass[i])):
            print(mass[i][i2], end=' ')
        print()

if oper == '8':
    astr = 'иванов:иван:иванович'
    a = input('Дана строка: "' + astr + '" Введите удаляемый символ: ')
    b = input('Введите символ подмены: ')
    astr2 = astr.replace(a, b)
    print(astr2)

if oper == '9':
    st = []
    num = []
    t = 'свалился, но ничего не помню, только тихо встал, и пошел в сторону дорог.'
    st = t.split(' ')
    for e in st:
        n = 5
        if (e.find(',') > 0) or (e.find('.') > 0): n = 6
        if len(e) == n:
            if n == 5: num.append(e[::-1])
            if (n == 6) and (e.find(',') > 0): num.append(e.replace(',', '')[::-1] + ',')
            if (n == 6) and (e.find('.') > 0): num.append(e.replace('.', '')[::-1] + '.')
        else:
            num.append(e)
    print(f'Исходный текст:\n {t}')
    print(" ".join(num))

if oper == '10':
    atext = 'Лег на храм, и дивен и невидим архангел'
    a = atext
    st = a.split()
    b = a.replace(' ', '')
    c = b.replace(',', '')
    a = c.lower()
    b = c[::-1].lower()
    print(f'Исходный текст "{atext}"')
    print(a)
    print(b)
    if a == b:
        print('True')
    else:
        print('False')
