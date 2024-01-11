def look(words):
    match words:
        case {'red': red, 'blue': blue}:
            print(f'{red}, {blue}')
        case {'red': 'Красный'}:
            print('Слово red есть в словаре, а слово blue отсутствует')
        case {'blue': 'Синий'}:
            print('Слово blue есть в словаре, а слово red отсутствует')
        case {}:
            print('Слова red и blue отсутствуют в словаре')
        case _:
            print('Это не словарь')


look({'red': 'Красный', 'blue': 'Синий', 'green': 'Зеленый'})
look({'red': 'Алый', 'blue': 'Синий', 'green': 'Зеленый'})
look({'red': 'Розовый', 'blue': 'Синий', 'green': 'Зеленый'})
# look({'red': 'Красный', 'green': 'Зеленый'})
# look({'blue': 'Синий', 'green': 'Зеленый'})
# look({'green': 'Зеленый'})
# look('red')

