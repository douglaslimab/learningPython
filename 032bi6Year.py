import datetime
year = int(input('Enter the year.\n'))
"""year = year % 100"""
if year == 0:
    year = datetime.date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('True for the year {}'.format(year))
else:
    print('False for the year {}'.format(year))