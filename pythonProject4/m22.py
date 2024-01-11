import datetime
from datetime import datetime
from datetime import timedelta
import locale

# date
# time
# datetime


# ys = datetime.date(2023, 1, 5)
#
# print('{}.{}.{}'.format(ys.day, ys.month, ys.year))
#
# tm = datetime.time(10, 24, 0)
# print(tm)

# dt = datetime(2023, 12, 25, 10, 26)

# print(dt)

# nw = datetime(2023, 1, 5, 10, 5)
#
# print(nw.date())
# print(nw.time())
#
# locale.setlocale(locale.LC_ALL, '')
#
# print(nw.strftime('%d.%m.%Y %H:%M:%S %B %A %p'))
# print(nw.strftime('%x %X'))

th = timedelta(hours=3, minutes=30)
print(th)

now = datetime.now()
print(now)

th = timedelta(hours=2)
nn = now + th

print(now)

if now < nn:
    print(f'{now} < {nn}')
if now.year == nn.year and now.month == nn.month:
    print(now.year)
