import datetime, locale

oldlocale = locale.setlocale(locale.LC_ALL, 'en')

locale.setlocale(locale.LC_CTYPE, 'chinese')

t1 = datetime.datetime.now()
t2 = t1.strftime('%Y年')

print(t2)

