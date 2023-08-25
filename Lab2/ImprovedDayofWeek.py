def dayOfWeekForDate(year, month, day):
    """
    Given year, month, and day, return the total number of days.
    
    :param year: int
    :param month: int
    :param day: int
    :return: int
    
    >>> dayOfWeekForDate(1752, 9, 30)
    5
    """
    year_remainder = (year % 100)
    step_two = year_remainder // 4
    step_four = step_two + day

    if (1 <= month <= 3):
        step_four += 144
    elif (4 <= month <= 6):
        step_four += 25
    elif (7 <= month <= 9):
        step_four += 36
    elif (10 <= month <= 12):
        step_four += 146
    
    curr_year_is_leap_year = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                curr_year_is_leap_year = True
        else:
            curr_year_is_leap_year = True
    
    if (curr_year_is_leap_year == True) and (month < 3):
        step_four -= 1
    
    if year >= 2000:
        step_four += 6
    elif year >= 1900:
        step_four += 0
    elif year >= 1800:
        step_four += 2
    elif year >= 1700:
        step_four += 4
        
    last_two_digits = str(year_remainder)
    digit_one = int(last_two_digits[-1])
    digit_two = int(last_two_digits[-2])
    sum_digits = digit_one + digit_two
    step_four += sum_digits
    day_num = step_four % 7
    
    return day_num
    
    
    
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
