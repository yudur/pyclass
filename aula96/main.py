"""
datetime
https://docs.python.org/2/library/datetime.html
"""
from datetime import datetime, timedelta

data = datetime.strptime('01/06/2022 21:21:00', '%d/%m/%Y %H:%M:%S')
data += timedelta(days=10, hours=10, seconds=500)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

print()

d1 = datetime.strptime('25/05/2019 20:45:32', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('12/01/2022 03:12:54', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(f'dias: {dif.days}     segundos: {dif.total_seconds()}')

print()

print(d1.time())
print(d1.date().strftime('%d/%m/%Y'))
