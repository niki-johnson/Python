"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month < 12:
        mes_dado = datetime.date(year, month, 1)
        prox_mes = datetime.date(year, month+1, 1)
        diff = prox_mes - mes_dado
        return diff.days
    else:
        mes_dado = datetime.date(year, month, 1)
        prox_mes = datetime.date(year+1, 1, 1)
        diff = prox_mes - mes_dado
        return diff.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    #data = datetime.date(year,month,day)
    if year > datetime.MAXYEAR or year < datetime.MINYEAR:
        return False
    elif month > 12 or month < 1:
        return False
    elif day > days_in_month(year, month) or day < 1:
        return False
    else:
        return True

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        dif = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
        if dif.days < 0 :
            return 0
        else:
            return dif.days
    else:
        return 0
    
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    todays = datetime.date.today()
    if not is_valid_date(year, month, day):
        return 0
    elif days_between(year, month, day, todays.year, todays.month, todays.day) < 0:
        return 0
    else:
        return days_between(year,month,day,todays.year,todays.month,todays.day)
    
print(is_valid_date(9998, 12, 31))