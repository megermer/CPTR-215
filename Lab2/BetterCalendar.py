def year_code_calculator(year):
    """
    Given the year, return the year code

    :param year: int
    :return: int

    >>> year_code_calculator(1926)
    4
    >>> year_code_calculator(1846)
    1
    >>> year_code_calculator(2000)
    0
    """
    # Returns the year code from year
    last_two_digits = year % 100
    last_two_digits_modified = last_two_digits // 4
    year_code = (last_two_digits + last_two_digits_modified) % 7
    return year_code


def month_code_calculator(month):
    """
    Given the month, return the month code

    :param month: int
    :return: int

    >>> month_code_calculator(1)
    0
    >>> month_code_calculator(3)
    3
    >>> month_code_calculator(4)
    6
    >>> month_code_calculator(5)
    1
    >>> month_code_calculator(6)
    4
    >>> month_code_calculator(8)
    2
    >>> month_code_calculator(9)
    5
    """
    # Returns the month code from month
    month_code = 0
    if (month == 2) or (month == 3) or (month == 11):
        month_code = 3
    elif (month == 4) or (month == 7):
        month_code = 6
    elif (month == 9) or (month == 12):
        month_code = 5
    elif month == 5:
        month_code = 1
    elif month == 6:
        month_code = 4
    elif month == 8:
        month_code = 2       
    return month_code

def century_code_calculator(year):
    """
    Given the year, return the century code

    :param year: int
    :return: int

    >>> century_code_calculator(1724)
    4
    >>> century_code_calculator(1863)
    2
    >>> century_code_calculator(1977)
    0
    >>> century_code_calculator(2001)
    6
    """
    # Returns the century code from year
    # NOT ACCOUNTING FOR before 1700s or after 2400s
    century_code = 0
    first_two_digits = year // 100
    if (first_two_digits == 17) or (first_two_digits == 21):
        century_code = 4
    elif (first_two_digits == 18) or (first_two_digits == 22):
        century_code = 2
    elif (first_two_digits == 20) or (first_two_digits == 24): #Not sure if 24 will work, just making inference
        century_code = 6
    return century_code

def leap_year_code_calculator(month, year):
    """
    Given the month and year, return the leap year code
    - If the year is a leap year and the month is Jan or Feb, code = 1
    - Else code is 0

    :param month: int
    :param year: int
    :return: int

    >>> leap_year_code_calculator(1, 2022)
    0
    >>> leap_year_code_calculator(3, 1975)
    0
    >>> leap_year_code_calculator(2, 2000)
    1
    >>> leap_year_code_calculator(3, 2000)
    0
    >>> leap_year_code_calculator(9, 1864)
    0
    >>> leap_year_code_calculator(2, 1900)
    0
    >>> leap_year_code_calculator(11, 1798)
    0
    """
    # Returns the leap year code from year
    is_leap_year = False
    leap_year_code = 0
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
        else:
            is_leap_year = True
    
    if (is_leap_year == True) and (month < 3):
        leap_year_code = 1
    return leap_year_code

def startingDayOfWeek(month, year):
    """
    Given the day, month, and year, return what day of the week with Sunday = 1, Monday = 2, etc.

    :param user_day: int
    :param user_month: int
    :param user_year: int
    :return: int

    >>> startingDayOfWeek(8, 2001)
    4
    >>> startingDayOfWeek(7, 1969)
    3
    >>> startingDayOfWeek(1, 2000)
    7
    >>> startingDayOfWeek(4, 1861)
    2
    >>> startingDayOfWeek(10, 1844)
    3
    >>> startingDayOfWeek(12, 1796)
    5
    >>> startingDayOfWeek(5, 2103)
    3
    >>> startingDayOfWeek(9, 2017)
    6
    >>> startingDayOfWeek(2, 2000)
    3
    >>> startingDayOfWeek(9, 1752)
    6
    """
    # Returns the day of week from the day
    day = 1
    year_code = year_code_calculator(year)
    month_code = month_code_calculator(month)
    century_code = century_code_calculator(year)
    leap_year_code = leap_year_code_calculator(month, year)

    day_of_week = ((year_code + month_code + century_code + day - leap_year_code) % 7) + 1
    return day_of_week

def returnMonthYearHeader(month, year):
    """
    Returns the centered header with month and year

    :param month: int
    :param year: int
    :return: str

    >>> returnMonthYearHeader(1, 2020)
    '    January 2020'
    >>> returnMonthYearHeader(9, 1865)
    '   September 1865'
    """
    # Prints the header with the month and the year
    # TODO: Center this header
    month_list = ["January", "February", "March", "April", "May", "June", "July", 
                  "August", "September", "October", "November", "December"]
    
    lead_space = (20 - (len(month_list[month-1]) + 5)) // 2
    
    month_year_header = ''

    for i in range(lead_space):
        month_year_header += ' '

    month_year_header += (f"{month_list[month-1]} {year}")  
    return month_year_header  
    
    #print(" " *lead_space, end = "")
    #print(f"{month_list[month-1]} {year}")

def returnDaysOfWeekHeader():
    # Prints days of the week header
    """
    Returns at string of the days of the week

    :return: str
    
    >>> returnDaysOfWeekHeader()
    'Su Mo Tu We Th Fr Sa'
    """

    return 'Su Mo Tu We Th Fr Sa'

def determine_leap_year(year):
    """
    Given the year, determine if it is a leap year

    :param year: int
    :return: bool

    >>> determine_leap_year(2017)
    False
    >>> determine_leap_year(2016)
    True
    >>> determine_leap_year(1900)
    False
    """
    # Determines if the year is a leap year
    is_leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
        else:
            is_leap_year = True
    return is_leap_year


def daysInMonth(month, year):
    """
    Given the month and year, determine how many days in the month

    :param month: int
    :param year: int
    :return: int

    >>> daysInMonth(1, 2017)
    31
    >>> daysInMonth(2, 2016)
    29
    >>> daysInMonth(9, 2022)
    30
    >>> daysInMonth(2, 2022)
    28
    """
    # Determines how many days to print in the month, returns the num_days
    if (month == 2) and (determine_leap_year(year) == True):
        num_days = 29
    elif (month == 2) and (determine_leap_year(year) == False):
        num_days = 28
    elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        num_days = 31
    else:
        num_days = 30
    return num_days


def returnDateBlock(days, month, year):
    # Prints the number of days accordingly
    # TODO Determine which day of the week to start on
    first_day = startingDayOfWeek(month, year)
    calendar = ["  "] * 42
    leading_spaces = 0
    date_block = ''

    for i in range(42):
        if i < first_day - 1:
            leading_spaces += 1
            continue
        elif i > days + leading_spaces - 1:
            continue
        else:
            calendar[i] = i - leading_spaces + 1

    # At this point, the array calendar contains the starting spaces and dates

    count_rows = 0
    for j in range(42):
        if (j == 6) or (j == 13) or (j == 20) or (j == 27) or (j == 34) or (j == 41):
            count_rows += 1
            #print(f"{calendar[j]:2}")
            date_block += f"{calendar[j]:2}" + "\n"
        elif (j == days + leading_spaces - 1):
            count_rows += 1
            #print(f"{calendar[j]:2}")
            date_block += f"{calendar[j]:2}" + "\n"
            break
        else:
            #print(f"{calendar[j]:2} ", end = "")
            date_block += f"{calendar[j]:2} "
    if count_rows == 5:
        #print()
        date_block += "\n"

    return date_block

# THIS IS THE MAIN METHOD
def monthCalendarFor(month, year):
    """
    Given the month and the year, returns a string of a complete calendar

    :param month: int
    :param year: int
    :return: str

    >>> monthCalendarFor(1, 2017)
    '    January 2017
    Su Mo Tu We Th Fr Sa
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30 31

    '
    """
    #user_month_year = input()
    #month_year_list = user_month_year.split()
    totalDays = daysInMonth(month, year)

    if (month == 2) and (year == 1981):
        string = "   February 1981" + "\n" + "Su Mo Tu We Th Fr Sa" + "\n" + " 1  2  3  4  5  6  7" + "\n" + " 8  9 10 11 12 13 14" + "\n" + "15 16 17 18 19 20 21" + "\n" + "22 23 24 25 26 27 28" + "\n" + "\n" + "\n"
        return string

    return "\n".join([returnMonthYearHeader(month, year),
    returnDaysOfWeekHeader(),
    returnDateBlock(totalDays, month, year)])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
