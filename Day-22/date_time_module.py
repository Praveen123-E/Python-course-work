'''

from datetime import date,time,datetime,timedelta

t=date.today()

print(t)
print("Year",t.year)
print("Month",t.month)
print("Day",t.day)
print("Weekday from 0:",t.weekday())
print("Weekday from 1:",t.isoweekday())

2026-06-23
Year 2026
Month 6
Day 23
Weekday from 0: 1
Weekday from 1: 2



from datetime import date

t=date(2026,5,13)
print(t)

2026-05-13


from datetime import time

t=time(12,22,34)
print(t)

#12:22:34
t=time(13,44,55)
print(t)

#13:44:55



from datetime import datetime

n=datetime.now()
print(n)

print("Year",n.year)
print("Month",n.month)
print("Day",n.day)
print("Hour",n.hour)
print("Minute:",n.minute)
print("Second:",n.second)

2026-06-23 11:39:55.904012
Year 2026
Month 6
Day 23
Hour 11
Minute: 39
Second: 55



from datetime import datetime

n=datetime.now()

print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))

print(n.strftime('%d %b %y %I:%M:%S %p'))
print(n.strftime('%d %B %y %I:%M:%S %p'))
print(n.strftime('%a, %d %B,%Y %I:%M:%S %p'))
print(n.strftime('%A, %d %B,%Y %I:%M:%S %p'))

23/06/26
23/06/26 11:51:36
23/06/26 11:51:36 AM
23 Jun 26 11:51:36 AM
23 June 26 11:51:36 AM
Tue, 23 June,2026 11:51:36 AM
Tuesday, 23 June,2026 11:51:36 AM


from datetime import timedelta,datetime

n=datetime.now()

n15=n+timedelta(minutes=15)
n2=n+timedelta(hours=2)
n7=n+timedelta(days=60)

print(n15,n2,n7,sep="\n")

2026-06-23 12:16:51.150421
2026-06-23 14:01:51.150421
2026-08-22 12:01:51.150421

'''


























