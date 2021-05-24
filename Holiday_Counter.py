# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:57:19 2021

@author: varun
"""
#importing the required libraries
from datetime import date,timedelta
import calendarific
import calendar
import numpy as np

# Here the user will enter the start and the end dates as string in YYYY-MM-DD format strictly.
# After which we will extract the individual date components to form a datetime object -> start_date and end_date


start_date_raw = input("Enter the start Date in YYYY-MM-DD format")
start_year,start_month, start_day = map(int,start_date_raw.split('-'))
start_date = date(start_year,start_month,start_day)


end_date_raw = input("Enter the end Date in YYYY-MM-DD format")
end_year,end_month,end_day  = map(int,end_date_raw.split('-'))
end_date = date(end_year,end_month,end_day)

#We prepare a list of all the years that may lie in the given period.
# We create an empty list of years, and add in the consecutive year till end_date.

year_list = []
for year in range(start_year,end_year+1):
    year_list.append(year)
    
# Creating the calendarific API object with my personal API key.

calapi = calendarific.v2('9b60083eb3526682d9c60dc07c6e2c9292b597ab')


events = []
event_dates = []

# Calling the API with the required parameters.
# Since we can have multiple years in our range -> the API doesn't allow to pass a list of years.
# Hence, we have to run the API call in a loop, for each year.

for year in year_list:
    
    parameters = {
	# Required
	'country': 'IN',
	'year':    year,}

    holidays = calapi.holidays(parameters)

  
    # Extracting the required entities from API response and selecting only the national holidays. 
    # Other options are - 'Optional holidays','Religion specific holidays'
    for i in range(len(holidays['response']['holidays'])):
        if('National holiday' in holidays['response']['holidays'][i]['type']):
            events.append(holidays['response']['holidays'][i]['name'])
            event_dates.append(holidays['response']['holidays'][i]['date']['iso'])
            
#Some of the holiday[....]['iso'] values contained time as well (Reason unknown) hence
# We restrict our string to 10 characters ----> YYYY-MM-DD = 10
holiday_dates = []
for val in event_dates:
    holiday_dates.append(val[:10])
        

#Events hold the name of the event/holiday.
#holiday_dates hold the dates of those events which are national holidays.
    
print(events)
print(holiday_dates)


delta = end_date-start_date
# total_days = delta.days

#np.busday_count returns the count of business days in a given date range.
#Since this application considers saturdays and sundays to be off.
total_days = np.busday_count(start_date,end_date)
total_days_with_weekends = delta.days



# for i in range(delta.days+1):
#     day = start_date+timedelta(days=i)
#     print(str(day))

count=0
#this keeps a track of holidays count.

# Iterate over all the dates that user provides, filter out dates which fall on weekends.
# Match if the date is present in the list of holiday dates.
#If yes, increase the counter.
# Final value of the counter is the total holidays except weekends, due to national holidays.

for i in range(delta.days+1):
    day = start_date+timedelta(days=i)
    if(calendar.day_name[day.weekday()] in ["Sunday","Monday"] ):
        continue
    #print(type(day))
    if(day.strftime("%Y-%m-%d") in holiday_dates):
        count+=1
        print(day.strftime("%Y-%m-%d")+' Occasion - ' + events[holiday_dates.index(day.strftime("%Y-%m-%d"))])


print(total_days-count, " Working days OUT of", total_days, "Business Days and", total_days_with_weekends," Total Days")

# for i in range(delta.days+1):
#     day = start_date+timedelta(days=i)
#     print(calendar.day_name[day.weekday()])
    
print(holidays)        





    




    
