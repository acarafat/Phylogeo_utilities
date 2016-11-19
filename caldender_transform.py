# Calender transform


from calendar import monthrange
from math import ceil
from datetime import datetime as dt
import time

def staging_fraction(decimal):
    '''
    1. Break decimal-date in usable format for transformDate
    2. Run transformDate
    3. Return date in yyyy-MM-dd format
    '''
    dec = str(decimal)
    if '.' in dec:
        y, d = dec.split('.')
        if d == '0':
            return str(int(decimal))+'-'+'01'+'-'+'01'
        d = float('.'+d)
        ny = int(y)
        output = transformDate(d, ny)
        return str(ny)+'-'+str(output[0])+'-'+str(int(output[1]))
    else:
        return str(decimal)+'-'+'01'+'-'+'01'
    

def transformDate(decimal, year):
    '''Transforming BEAST date output
    from point decimals to calender dates
    Example:
    >>> transformDate( .61748634, 2016)
    (8, 14.0)
    '''
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
    '''
    Example:
    >>> toYearFraction(dt(2016, 11, 13))
    2016.8661202185792
    '''
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
