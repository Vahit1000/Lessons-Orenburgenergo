# Задание 5
# Проверка слова/текста на палиндром
# Примеры
# радар
# шалаш

text = 'Лег на храм, и дивен и невидим архангел'

symbols = ' ,.!@#$%><{}[]()'
s = ''.join(x for x in list(text) if x not in symbols).lower()
print(f'{text} - этот текст {'палиндром' if s == s[::-1] else 'не палиндром'}' )


