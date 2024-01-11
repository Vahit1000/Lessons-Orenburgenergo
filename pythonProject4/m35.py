import locale

locale.setlocale(locale.LC_ALL, 'us')

n = 12345.678
ft = locale.format_string('%f', n)
print(n)
print(locale.currency(n))
print(locale.getlocale())




