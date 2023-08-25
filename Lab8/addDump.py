def __add__(self, addend):
        """
        >>> Date(2004, 2, 18) + 365
        Date(2005, 2, 17)
        >>> Date(2004, 3, 18) + 365
        Date(2005, 3, 18)
        >>> Date(2004, 2, 18) + 368
        Date(2005, 2, 20)
        >>> Date(2004, 2, 18) + 1500
        Date(2008, 3, 28)
        >>> Date(2004, 2, 18) + 3000
        Date(2012, 5, 6)
        >>> Date(2004, 2, 18) + 4461
        Date(2016, 5, 6)
        >>> Date(2004, 2, 18) + 5191
        Date(2018, 5, 6)
        """
        years_from_addend = addend // 365
        days_from_addend = addend % 365
        leap_year_days = 0
        count_sandwich_leapyears = 0
        for year in range(self.year + 1, self.year + years_from_addend):
            if Date(year, self.month, self.day).is_leap_year():
                leap_year_days += 1
                count_sandwich_leapyears += 1
        if (self.is_leap_year()) and (self.month < 3):
            leap_year_days += 1
        if ((Date(self.year + years_from_addend, self.month, self.day).is_leap_year()) and (self.month >= 3)):
            leap_year_days += 1
        for i in range(leap_year_days + days_from_addend - 1):
            self = self.next_day()
        revised_date = Date(self.year, self.month, self.day)
        for i in range(leap_year_days):
            revised_date = revised_date.previous_day()

        revised_date = Date(self.year + years_from_addend, revised_date.month, revised_date.day)
        return revised_date
    
    def __add__(self, addend):
        """
        >>> Date(2004, 2, 18) + 365
        Date(2005, 2, 17)
        >>> Date(2004, 3, 18) + 365
        Date(2005, 3, 18)
        >>> Date(2004, 2, 18) + 368
        Date(2005, 2, 20)
        >>> Date(2004, 2, 18) + 1500
        Date(2008, 3, 28)
        >>> Date(2004, 2, 18) + 3000
        Date(2012, 5, 6)
        >>> Date(2004, 2, 18) + 4461
        Date(2016, 5, 6)
        >>> Date(2004, 2, 18) + 5191
        Date(2018, 5, 6)
        """
        years_from_addend = addend // 365
        days_from_addend = addend % 365
        leap_year_days = 0
        count_sandwich_leapyears = 0
        for year in range(self.year + 1, self.year + years_from_addend):
            if Date(year, self.month, self.day).is_leap_year():
                leap_year_days += 1
                count_sandwich_leapyears += 1
        if (self.is_leap_year()) and (self.month < 3):
            leap_year_days += 1
        if ((Date(self.year + years_from_addend, self.month, self.day).is_leap_year()) and (self.month >= 3)):
            leap_year_days += 1
        revised_date = Date(self.year, self.month, self.day)
        for i in range(leap_year_days + days_from_addend - 1):
            revised_date = revised_date.next_day()
        for i in range(leap_year_days):
            revised_date = revised_date.previous_day()

        revised_date = Date(self.year + years_from_addend, revised_date.month, revised_date.day)
        return revised_date
    
    def __add__(self, addend):
        """
        >>> Date(2004, 2, 18) + 3000
        Date(2012, 5, 6)
        >>> Date(2004, 2, 18) + 4461
        Date(2016, 5, 6)
        >>> Date(2004, 2, 18) + 5191
        Date(2018, 5, 6)
        """
        years_from_addend = addend // 365
        days_from_addend = addend % 365
        leap_year_days = 0
        count_sandwich_leapyears = 0
        for year in range(self.year + 1, self.year + years_from_addend):
            if Date(year, self.month, self.day).is_leap_year():
                leap_year_days += 1
                count_sandwich_leapyears += 1
        if (self.is_leap_year()) and (self.month < 3):
            leap_year_days += 1
        if ((Date(self.year + years_from_addend, self.month, self.day).is_leap_year()) and (self.month >= 3)):
            leap_year_days += 1
        revised_date = Date(self.year, self.month, self.day)
        for i in range(leap_year_days + days_from_addend - 1):
            revised_date = revised_date.next_day()
        for i in range(leap_year_days):
            revised_date = revised_date.previous_day()
        print(f"Years from addend: {years_from_addend}")
        print(f"Days from addend: {days_from_addend}")
        print(f"Leap year days: {leap_year_days}")
        print(f"Count sandwich leapyears: {count_sandwich_leapyears}")

        revised_date = Date(self.year + years_from_addend, revised_date.month, revised_date.day)
        return revised_date
    
    def __add__(self, addend):
        """
        >>> Date(2004, 2, 18) + 3000
        Date(2012, 5, 6)
        >>> Date(2004, 2, 18) + 4461
        Date(2016, 5, 6)
        >>> Date(2004, 2, 18) + 5191
        Date(2018, 5, 6)
        >>> Date(2005, 1, 2) + 1
        Date(2005, 1, 3)
        """
        years_from_addend = addend // 365
        days_from_addend = addend % 365
        leap_year_days = 0
        local_date = self
        year_start = Date(self.year, 1, 1)
        
        while local_date > year_start:
            local_date = local_date.previous_day()
            days_from_addend += 1
        local_date = Date(self.year + years_from_addend, local_date.month, local_date.day)
        for day in range(days_from_addend):
            local_date = local_date.next_day()
        #for year in range(self.year, local_date.year + 1):
        #    if Date(year, 1, 1).is_leap_year():
        #        leap_year_days += 1
        #for i in range(leap_year_days):
        #    local_date = local_date.previous_day()
        return local_date