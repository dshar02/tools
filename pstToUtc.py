import datetime
import dateutil.tz
from dateutil.parser import parse

flag = 0
answer = 'n'

while flag == 0:
    string = input('Enter Pacific Time date in the format YYYY-MM-DD: ')
    date = parse(string)

    midnight = (datetime.datetime
        (date.year, date.month, date.day, 0, 0, 0, 0, dateutil.tz.gettz('US/Pacific'))
        .astimezone(dateutil.tz.tzutc()))

    print(midnight, end = ' UTC')
    print()

    answer = input('Convert another date? y or n: ')
    if answer == 'y':
        flag = 0
    else:
        flag = 1

