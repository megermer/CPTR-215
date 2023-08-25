# Meg Ermer
# CPTR 215, Lab 8b
# History
#	1 November 2022: Added testing, documentation
#	27 October 2022: Implemented the idea of orienting myself in relation to leapdays. Things got much better. Finished rest of methods.
#					 Added documentation.
#	26 October 2022: Started. Cried. Got no sleep. Finished init, repr, string, gt, e, lt
# Sources
#	First 10 methods from Warmup 5
class Date:
    def __init__(self, year, month, day):
        """Initializes a date given a year, month, and day. 
        >>> today = Date(2021, 9, 27)
        >>> today.day
        27
        >>> Date(1776, 7, 4).year
        1776
        """
        self.year = year
        self.month = month
        self.day = day
        
    def __repr__(self):
        """Returns a string that would evaluate to an identical Date object.
        >>> Date(2021, 9, 29).__repr__() # not common
        'Date(2021, 9, 29)'
        >>> Date(1970, 12, 31)
        Date(1970, 12, 31)
        >>> repr(Date(1984, 2, 20))
        'Date(1984, 2, 20)'
        """
        return f"Date({self.year}, {self.month}, {self.day})"
    
    def __str__(self):
        """Returns a human-readable string representation of self
        in MMM d, yyyy format.
        >>> Date(2000, 1, 1).__str__() # not common
        'Jan 1, 2000'
        >>> str(Date(2021, 9, 27))
        'Sep 27, 2021'
        >>> independence = Date(1776, 7, 4)
        >>> print(independence)
        Jul 4, 1776
        """
        month_name = "BAD Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()[self.month]
        return f"{month_name} {self.day}, {self.year}"
    
    def is_leap_year(self):
        """Determines whether self is in a leap year.
                    Truth Table
            4s place  2s place  1s place
             div 4 | div 100 | div 400 | leap?
            -------+---------+---------+-------
               0         0         0       0
               0         0         1       X
               0         1         0       X
               0         1         1       X
               1         0         0       1
               1         0         1       X
               1         1         0       0
               1         1         1       1
        >>> Date(2021, 9, 29).is_leap_year()
        False
        >>> Date(1984, 4, 27).is_leap_year()
        True
        >>> Date(2000, 1, 1).is_leap_year()
        True
        >>> Date(1900, 11, 30).is_leap_year()
        False
        """
        return self.year % 400 == 0 or \
               (self.year % 4 == 0 and self.year % 100 != 0)
    
    def next_day(self):
        """ Returns the next day of a given Date
        >>> Date(2022, 3, 14).next_day()
        Date(2022, 3, 15)
        >>> Date(1935, 10, 31).next_day()
        Date(1935, 11, 1)
        >>> Date(1897, 12, 31).next_day()
        Date(1898, 1, 1)
        >>> Date(1996, 2, 28).next_day()
        Date(1996, 2, 29)
        >>> Date(1997, 2, 28).next_day()
        Date(1997, 3, 1)
        >>> Date(1997, 12, 31).next_day()
        Date(1998, 1, 1)
        >>> Date(1936, 1, 31).next_day()
        Date(1936, 2, 1)
        >>> Date(1872, 4, 30).next_day()
        Date(1872, 5, 1)
        >>> Date(2017, 2, 28).next_day()
        Date(2017, 3, 1)
        >>> Date(2019, 8, 26).next_day()
        Date(2019, 8, 27)
        """
        year = self.year
        month = self.month
        day = self.day
        if day == 31: #Handles going forward to next month cases
            if month == 12: #Dec. 31 -> Jan. 1
                return Date(year + 1, 1, 1)
            else: #Handles 31-day going forward-into-next-month cases
                return Date(year, month + 1, 1)
        elif day == 30: #Handles 30-day month going forward to next month cases
            if (month == 4) or (month == 6) or (month == 9) or (month == 11): 
                return Date(year, month + 1, 1)
        if ((month == 2) and (day == 28) and (self.is_leap_year() != True)) or ((month == 2) and (day == 29)): #Handles leapday and Feb 28 cases
            return Date(year, 3, 1)
        return Date(year, month, day + 1) #All other normal cases
    
    def previous_day(self):
        """ Returns the previous day of a given Date
        >>> Date(2000, 4, 1).previous_day()
        Date(2000, 3, 31)
        >>> Date(2000, 3, 1).previous_day()
        Date(2000, 2, 29)
        >>> Date(2021, 9, 6).previous_day()
        Date(2021, 9, 5)
        >>> Date(1874, 7, 1).previous_day()
        Date(1874, 6, 30)
        >>> Date(1785, 1, 1).previous_day()
        Date(1784, 12, 31)
        >>> Date(2016, 3, 1).previous_day()
        Date(2016, 2, 29)
        >>> Date(2017, 3, 1).previous_day()
        Date(2017, 2, 28)
        >>> Date(2018, 5, 2).previous_day()
        Date(2018, 5, 1)
        >>> Date(2016, 2, 29).previous_day()
        Date(2016, 2, 28)
        """
        year = self.year
        month = self.month
        day = self.day
        if day == 1: #Handles going back to previous month cases
            if (month == 2) or (month == 4) or (month == 6) or (month == 8) or (month == 9) or (month == 11): #Feb, Apr, Jun, Aug, Sept, Nov
                return Date(year, month - 1, 31)
            elif (month == 5) or (month == 7) or (month == 10) or (month == 12): #May, Jul, Oct, Dec.
                return Date(year, month - 1, 30)
            elif (month == 1): #Jan 1 -> Dec. 31
                return Date(year - 1, 12, 31)
            elif (month == 3):#March -> Feb. 28 or leapday
                if self.is_leap_year() == True:
                    return Date(year, 2, 29)
                else:
                    return Date(year, 2, 28)
        return Date(year, month, day - 1) #All other cases
    
    def __gt__ (self, other):
        """ Returns if the self date is greater than the other date
        >>> Date(2024, 9, 3) > Date(2024, 8, 9)
        True
        >>> Date(2024, 8, 9) > Date(2024, 9, 3)
        False
        >>> Date(2024, 8, 2) > Date(1900, 9, 3)
        True
        >>> Date(2024, 8, 2) > Date(2025, 3, 1)
        False
        >>> Date(1900, 9, 2) > Date(1900, 12, 13)
        False
        >>> Date(2000, 8, 15) > Date(2000, 8, 13)
        True
        >>> Date(2000, 8, 15) > Date(2000, 8, 10)
        True
        """
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month: #Same year, different month
                return True
            if self.month == other.month:
                if self.day > other.day: #Same year and month, different day
                    return True
        return False
    
    def __lt__(self, other):
        """ Determines if self Date is less than (earlier) than the other
        >>> Date(2024, 9, 3) < Date(2024, 8, 9)
        False
        >>> Date(2024, 8, 9) < Date(2025, 9, 3)
        True
        >>> Date(2026, 8, 9) < Date(2025, 9, 3)
        False
        >>> Date(2024, 10, 9) < Date(2024, 9, 3)
        False
        >>> Date(2024, 8, 1) < Date(2025, 8, 3)
        True
        >>> Date(2025, 8, 9) < Date(2025, 8, 3)
        False
        """
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month: #Same year, different month
                return True
            if self.month == other.month:
                if self.day < other.day: #Same year, same month, different day
                    return True
        return False
    
    def __eq__(self, other):
        """ Determines if self date is equal to another date
        >>> Date(2024, 9, 3) == Date(2024, 9, 3)
        True
        >>> Date(2024, 9, 3) == Date(2024, 9, 2)
        False
        >>> Date(2025, 9, 3) == Date(2024, 8, 3)
        False
        """
        return (self.year == other.year) and (self.month == other.month) and (self.day == other.day)
   
    
    def __ge__(self, other):
        """ Determines of self date is greater than or equal to another date
        >>> Date(2024, 9, 3) >= Date(2024, 9, 2)
        True
        >>> Date(2025, 10, 12) >= Date(2025, 10, 13)
        False
        """
        return (self > other) or (self == other)
    
    
    def __add__(self, addend):
        """ Adds a certain amount of days to a given Date
        >>> Date(2004, 2, 18) + 3000
        Date(2012, 5, 6)
        >>> Date(2004, 2, 18) + 4461
        Date(2016, 5, 6)
        >>> Date(2004, 2, 18) + 5191
        Date(2018, 5, 6)
        >>> Date(2005, 1, 2) + 1
        Date(2005, 1, 3)
        >>> Date(1999, 8, 27) + 9375
        Date(2025, 4, 27)
        >>> Date(1897, 9, 21) + 3234
        Date(1906, 7, 31)
        >>> Date(3823, 3, 11) + -834
        Date(3820, 11, 27)
        """
        if addend < 0:
            return self - -addend #If addend is negative, turns expression into subtraction and passes it to the __sub__ method
        years_from_addend = addend // 365 #Finds number of whole years from the addend
        days_from_addend = addend % 365 #Finds remainder of days from addend
        leap_year_days = 0 
        local_date = self
        while (local_date.month != 2) or (local_date.day !=29): #Finds the closest previous leapday... 
            local_date = local_date.previous_day()
            days_from_addend += 1 #...and counts the number of days away that is, adding it to the days_from_addend
        for year in range(years_from_addend): #Iterates through the years_from_addend, if that year is a leap year, takes away a day to account for the "leap"
            if local_date.is_leap_year():
                local_date = local_date.previous_day()
            local_date = Date(local_date.year + 1, local_date.month, local_date.day) #Reassigns local_date to exactly a year later
        for day in range(days_from_addend): #Calls next_day() for each day in days_from_addend
            local_date = local_date.next_day()
        return local_date
        
    def find_previous_leapday(self):
        """ Determines the closest previous leapday to a given Date, returning an array with the amount of days since that leapday and the leapday
        >>> Date(2019, 8, 12).find_previous_leapday()
        [1260, Date(2016, 2, 29)]
        >>> Date(1749, 2, 13).find_previous_leapday()
        [350, Date(1748, 2, 29)]
        """
        count_days = 0
        local_date = self
        while (local_date.month != 2) or (local_date.day != 29):
            local_date = local_date.previous_day()
            count_days += 1
        return [count_days, local_date]
    
    def find_next_leapday(self):
        """ Determines the closest next leapday to a given Date, returning an array with the amount of days since that leapday and the leapday
        >>> Date(2019, 8, 12).find_next_leapday()
        [201, Date(2020, 2, 29)]
        >>> Date(1749, 2, 13).find_next_leapday()
        [1111, Date(1752, 2, 29)]
        """
        count_days = 0
        local_date = self
        while (local_date.month != 2) or (local_date.day != 29):
            local_date = local_date.next_day()
            count_days += 1
        return [count_days, local_date]
    
    def sub_dates(self, other):
        """ Handles subtracting a date from another date (finds the offset, with a positive or negative int indicating the direction)
        >>> Date(1942, 12, 25).sub_dates(Date(2002, 3, 19))
        -21634
        >>> Date(1776, 1, 29).sub_dates(Date(1865, 4, 3))
        -32571
        """
        previous_leapday = self.find_previous_leapday()[1] #Finds the closest previous leapday of the earlier date
        days_since_previous_leapday = self.find_previous_leapday()[0] #Finds the amount of days since that previous leapday
        next_leapday = other.find_next_leapday()[1] #Finds the closest next leapday of the later date
        days_til_next_leapday = other.find_next_leapday()[0] #Finds the amount of days until that next leapday
        interval_1461 = 0 #Keeps track of the times that we need to add 1461 days (this occurs between normal, 4-year-apart leapdays)
        interval_2921 = 0 #Keeps track of the times that we need to add 2921 days (this occurs between leap years that have a non-leap year century year between them)
        for year in range(previous_leapday.year, next_leapday.year): #Iterates between the previous leapday year and the next leapday year
            if Date(year, 1, 1).is_leap_year(): #If that year is a leapyear...
                interval_1461 += 1 #...increment the interval_1461 by 1
                if not Date(year + 4, 1, 1).is_leap_year(): #If, in four years, it is not a leap year (ex. 1896 -> 1900)...
                    interval_1461 -= 1 #... you won't be incrementing by 1461...
                    interval_2921 += 1 #... you will be incrementing by 2921 instead
        return -((interval_1461 * 1461) + (interval_2921 * 2921) - (days_since_previous_leapday + days_til_next_leapday))
        #Return the distance between those two leapdays, minus the distance between the earlier date and previous leapday, and the distance between the later date and the next leapday
        
    def __sub__(self, subtrahend):
        """
        >>> Date(2022, 4, 20) - 1
        Date(2022, 4, 19)
        >>> Date(2022, 3, 18) - 365
        Date(2021, 3, 18)
        >>> Date(2022, 5, 30) - -1
        Date(2022, 5, 31)
        >>> Date(1942, 8, 30) - Date(1942, 8, 30)
        0
        >>> Date(1941, 8, 30) - Date(1942, 8, 30)
        -365
        >>> Date(1895, 9, 2) - Date(1901, 4, 15)
        -2051
        >>> Date(1999, 12, 2) - Date(2001, 1, 15)
        -410
        >>> Date(2001, 1, 15) - Date(1999, 12, 2)
        410
        >>> Date(1901, 4, 15) - Date(1895, 9, 2)
        2051
        >>> Date(1942, 8, 30) - Date(1941, 8, 30)
        365
        """
        if (type(subtrahend) == int) and (subtrahend > 0): #Handles offset subtraction cases
            years_from_subtrahend = subtrahend // 365 #Finds number of whole years from subtrahend
            days_from_subtrahend = subtrahend % 365 #Finds remaining number of days from subtrahend
            leap_year_days = 0 
            local_date = self
            while (local_date.month != 2) or (local_date.day != 29): #Finds the closest next leapday...
                local_date = local_date.next_day() 
                days_from_subtrahend += 1 #...and counts the number of days away that it is, adding those to the days_from_subtrahend
            for i in range(years_from_subtrahend): #Iterates through the years_from_subtrahend, and if the year is a leapyear, adds a day to account for the "leap"
                if local_date.is_leap_year():
                    local_date = local_date.next_day()
                local_date = Date(local_date.year - 1, local_date.month, local_date.day) #Reassigns local_date to exactly a year earlier
            for day in range(days_from_subtrahend):
                local_date = local_date.previous_day() #Calls previous_day() for each of the days in days_from_subtrahend
            return local_date
        elif (type(subtrahend) == int) and (subtrahend <= 0): #If the subtrahend is 0 or negative, passes it to the __add__ method
            return self + -subtrahend
        else: #Handles subtracting dates from other dates
            if self == subtrahend:
                return 0
            elif self < subtrahend:
                return self.sub_dates(subtrahend)
            elif self > subtrahend:
                return -(subtrahend.sub_dates(self))
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()    
    
    
