# BEAST Utilis

from calendar import monthrange
from math import ceil
from datetime import datetime as dt
import time


def transformDate(decimal, year):
    '''Transforming BEAST date output
    from point decimals to calender dates'''
    
    if monthrange(year, 2) == 28:
        days = 365*decimal
    else:
        days = 366*decimal

    for i in range(1, 13):
        try:        
            days = days - monthrange(year, i)[1]
            if days < monthrange(year, i+1)[1]:
                return (i+1, ceil(days))
        except:
            return (i, ceil(days))
        

def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction
