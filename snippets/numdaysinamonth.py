#!/usr/bin/env python3

# code to find the number of days in a month

import calendar

def getMonthDays(month, year):
    # returns the number of days in a month
    intmonth = int(month)
    intyear = int(year)
    if month == 1:  # Check to see if the month is January, if it is then we need to take a year from the year
        myear = intyear - 1
        mmonth = 12
    else:
        myear = intyear
        mmonth = intmonth - 1

    lastmonth = calendar.monthrange(myear, mmonth)
    data = [lastmonth[1], myear, mmonth]
    return data


data1 = getMonthDays(3,  2019)
print(data1)
print("The last month, " + str(data1[2]) + " contained " + str(data1[0]) + " days, and the year is " + str(data1[1]))
