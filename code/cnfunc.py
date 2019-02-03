#!/usr/bin/env paython3

# Copyright 2019 by Chuck Nelson

# This file contains functions for the Audio Copy Pro application.

import calendar

def getMonthFromText(month):
    """
        Returns the number of the month in string from the 3 letter abbreviations
    """
    if month == 'Jan':
        return "1"
    elif month == 'Feb':
        return '2'
    elif month == 'Mar':
        return '3'
    elif month == 'Apr':
        return '4'
    elif month == 'May':
        return '5'
    elif month == 'Jun':
        return '6'
    elif month == 'Jul':
        return '7'
    elif month == 'Aug':
        return '8'
    elif month == 'Sep':
        return '9'
    elif month == 'Oct':
        return '10'
    elif month == 'Nov':
        return '11'
    elif month == 'Dec':
        return '12'
    else:
        return False

def getMonthFromNum(month):
    """
        Returns the three letter abreviation for a month
    """
    if month == 1:
        return "Jan"
    elif month == 2:
        return "Feb"
    elif month == 3:
        return "Mar"
    elif month == 4:
        return "Apr"
    elif month == 5:
        return "May"
    elif month == 6:
        return "Jun"
    elif month == 7:
        return 'Jul'
    elif month == 8:
        return 'Aug'
    elif month == 9:
        return 'Sep'
    elif month == 10:
        return 'Oct'
    elif month == 11:
        return 'Nov'
    elif month == 12:
        return 'Dec'
    else:
        return 'Month'

def menuSelectFileSave(event = None):
    print("Save Mass Info initiated...")

# **** RUN Menu Items


# Generic Methods
def testRun(event = None):
    print('Check box clicked...')
    print(event)

def getMonthDays(month, year):
    # returns the number of days in a month
    intmonth = int(month)
    intyear = int(year)
    # print("Tested: [" + str(intmonth) + "]")
    if intmonth == 1:  # Check to see if the month is January, if it is then we need to take a year from the year
        myear = intyear - 1
        mmonth = 12
    else:
        myear = intyear
        mmonth = intmonth - 1
    # print("Test 2: [" + str(mmonth) + "]")
    lastmonth = calendar.monthrange(myear, mmonth)
    data = [lastmonth[1], myear, mmonth]
    return data
