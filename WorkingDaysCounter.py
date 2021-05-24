# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:42:27 2021

@author: varun
"""
#importing the required libraries
from datetime import date,timedelta
import calendarific
import calendar
import numpy as np

def input_start_date():
    
    """
    User will input the start date, strictly in YYYY-MM-DD format
    """
    
    
    start_date_raw = input("Enter the start Date in YYYY-MM-DD format")
    start_year,start_month, start_day = map(int,start_date_raw.split('-'))
    start_date = date(start_year,start_month,start_day)
    return start_date

def input_end_date():
    """
    User will input the end date, strictly in YYYY-MM-DD format
    """
    end_date_raw = input("Enter the end Date in YYYY-MM-DD format")
    end_year,end_month,end_day  = map(int,end_date_raw.split('-'))
    end_date = date(end_year,end_month,end_day)
    return end_date


def find_total_days(start_date,end_date):
    
    """
    This function will return the net number of days and total business days given a range.
    Business days are days from [Monday to Friday]
    Net days = business Days + [Saturday, Sunday]
    """
    
    delta = end_date-start_date
    total_business_days = np.busday_count(start_date,end_date)
    total_days = delta.days #Returns the TOTAL days in the range
   
    return total_days,total_business_days

def find_national_holidays(start_date,end_date):
    
    """
    1) We start off by creating a Calendarific API object using unique API key.
    2) Since a user may enter a range comprising of multiple years, we extract the year
       from the input datetime objects and call the API iteratively for all the years.
    3) Once the holidays are extracted, we store only the HOLIDAYS with TYPE - NATIONAL HOLIDAY,
       along with their date and event name.
    4) Some of the holiday dates returned by the API also contained time (reason unknown) hence 
       to avoid any issues, these were truncated to 10 characters (YYYY-MM-DD)
    5) A counter was intialized, to count the holidays which falled on business days.
    6) Each date (non-weekend) in the given date ranage was iterated and matched against holiday dates
       and counter was incremented if a match was found.
    7) Information of the events was extracted based in index from the events list prepared earlier.
    8) Results were shown.
    
    """
    
    delta = end_date-start_date
    year_list = []
    for year in range(start_date.year,(end_date.year)+1):
        year_list.append(year)
    calapi = calendarific.v2('9b60083eb3526682d9c60dc07c6e2c9292b597ab')
    events = []
    event_dates = []
    holiday_dates = []
    
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
                
    
    occasion=[]
    for val in event_dates:
        holiday_dates.append(val[:10])
    
    count = 0
    for i in range(delta.days+1):
        day = start_date+timedelta(days=i)
        if(calendar.day_name[day.weekday()] in ["Sunday","Saturday"] ):
            continue
        #print(type(day))
        if(day.strftime("%Y-%m-%d") in holiday_dates):
            count+=1
            occasion.append(day.strftime("%Y-%m-%d")+' Occasion - ' + events[holiday_dates.index(day.strftime("%Y-%m-%d"))])
            
    return count,occasion    

    
    
    
    
if __name__=='__main__':
    
    #Main Function/Driver Code
    
    
    
    
    def print_menu():
           
        print("\n-------WELCOME TO WORKING DAYS COUNTER APPLICATION-------\n")
        print("PLease make a choice \n")
        print("1.Find the Working days in given period\n")
        print("2.Exit\n")
        
    
        
    # start_date = input_start_date()
    # end_date = input_end_date()
    # net_days,net_bus_days = find_total_days(start_date,end_date)
    # count, occasion = find_national_holidays(start_date,end_date,holiday_dates)
    
    
    while(True):
        print_menu()
        choice = int(input("\nEnter your choice\n"))
        
        if(choice == 1):
            start_date = input_start_date()
            end_date = input_end_date()
            net_days,net_bus_days = find_total_days(start_date,end_date)
            count, occasion = find_national_holidays(start_date,end_date)
            print("\nOut of total :",net_days,", there are :",net_bus_days," business days and ", net_bus_days-count," Working days.\n")
            print("Following holidays are encountered in the given period \n")
            print("Note: Only holidays which occur on a business day are listed \n")
            for item in occasion:
                print(item,'\n')
            continue
        
         
        elif(choice==2):
                      
            break
    
    print("----------Thanks for using this application-----------\n")
    print("---           created by Varun Gupta           ------\n")
        
            
        
        
            
            
            
            
            
                
            
            
            
            
            
    
    
    
