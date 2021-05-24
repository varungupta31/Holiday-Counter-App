# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:37:59 2021

@author: varun
"""

import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2021,3)
print(str)

c = calendar.TextCalendar(calendar.THURSDAY)
str = c.formatmonth(2021,3)
print(str)

hc = calendar.HTMLCalendar(calendar.THURSDAY)
str = hc.formatmonth(2021,1)
print(str)

for i in c.itermonthdays(2021,3):
    print(i)
    
for i in c.itermonthdays(2021,4):
    print(i)
    
count=0
for i in c.itermonthdays(2021,4):
    if(i!=0):
        count+=1;
print(count)
    
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)
    

from datetime import date, timedelta
f_date = date(2021,3,1)
l_date = date(2021,5,16)
delta = (l_date-f_date)
print(delta)
print(delta.days)

for i in range(delta.days +1):
    day = f_date + timedelta(days=i)
    print(day)
    


import calendarific

calapi = calendarific.v2('9b60083eb3526682d9c60dc07c6e2c9292b597ab')

parameters = {
	# Required
	'country': 'IN',
	'year':    2021,
}

holidays = calapi.holidays(parameters)

type(holidays)

print(holidays['response']['holidays'][0]['name'])
print(holidays['response']['holidays'][0]['date']['iso'])


