def dayOfWeekForDate(year, month, day):
    """
    Given year, month, and day, return the total number of days.
    
    :param year: int
    :param month: int
    :param day: int
    :return: int
    
    >>> dayOfWeekForDate(1595, 1, 28)
    7
    """
    
    # finds the number of days in given amount of years, accounting for leap years, and finds if current year is leap year
    curr_year_is_leap_year = False
    
    num_leap_years = 0;
    for i in range(1595, year):
        if i % 4 == 0:
            if i % 100 == 0:
                if i % 400 == 0:
                    num_leap_years += 1
                    curr_year_is_leap_year = True
            else:
                num_leap_years +=1
                curr_year_is_leap_year = True
                
    days_for_years = ((year - 1595) * 365) + num_leap_years
    
    
    # finds the number of days in given amount of months, accounting for leap years
    days_for_months = 0

    for j in range(month - 1):
        if (j == 0) or (j == 2) or (j == 4) or (j == 6) or (j == 7) or (j == 9) or (j == 11):
            days_for_months += 31
        elif j == 1:
            days_for_months += 28
        else:
            days_for_months += 30
    
    # finds the total number of days, accounting if current year is a leap year and date is AFTER february 
    total_days = days_for_years + days_for_months + day
    
    if curr_year_is_leap_year == True:
        if (month > 2):
            total_days += 1
    if total_days % 7 == 0:
        total_days += 7
    day_of_week = (total_days % 7)
    return day_of_week
    
    
def nameForDayOfWeekNumber(day_number):
    """
    Given a number corresponding to a day of the week, return the written day.
    
    :param day_number: int
    :return: string
    
    >>> nameForDayOfWeekNumber(7)
    'Sabbath'
    """
    if day_number == 1:
        return "Sunday"
    if day_number == 2:
        return "Monday"
    if day_number == 3:
        return "Tuesday"
    if day_number == 4:
        return "Wednesday"
    if day_number == 5:
        return "Thursday"
    if day_number == 6:
        return "Friday"
    if day_number == 7:
       return "Sabbath"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)