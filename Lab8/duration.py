# Meg Ermer
# CPTR 215 A, Lab 9A
# History:
#	1 November: documentation, fine combing
#	26 October: better __init__, add, sub, 
#	25 October: first draft, rough __init__

class Duration:
    def __init__(self, param1, param2 = None, param3 = None):
        """ Initializes a Duration object to have hours, minutes, and seconds. Also includes non-represented fields total_seconds and is_negative
        >>> Duration(23, 59, 59)
        Duration('23:59:59')
        >>> Duration("1:30:00")
        Duration('1:30:00')
        >>> Duration("0d0h45s")
        Duration('0:00:45')
        """
        self.is_negative = False
        if type(param1) == int: #Transforms int parameter cases into the standard ('hr:min:sec')
            if type(param2) == int:
                param_list = [str(param1), str(param2), str(param3)]
                duration_string = ":".join(param_list)
            else:
                duration_string = f"{param1}s" #If there is only one int, it is in seconds
        else:
            duration_string = param1
        if duration_string[0] == "-": #Checks for negative Duration objects
            self.is_negative = True
            duration_string = duration_string[1:]
        
        standards = {
            "d": 86400,
            "h": 3600,
            "m": 60,
            "s": 1
        }
        
        if ":" in duration_string: 
            duration_list = duration_string.split(":")
            self.total_seconds = (int(duration_list[0]) * 3600) + (int(duration_list[1]) * 60) + (int(duration_list[2])) #Assigning hours, minutes, seconds, and total_seconds
        else:
            self.total_seconds = 0
            for i in standards:
                if i in duration_string:
                    i_index = duration_string.index(i)
                    self.total_seconds += int(duration_string[0:i_index]) * standards[i]
                    duration_string = duration_string[i_index+1:]
        # Calculates the hours, minutes, and seconds from total_seconds -- would be a loop except I need to assign fields and this isn't possible in a loop
        total_seconds_local = self.total_seconds
        self.hours = total_seconds_local // 3600
        total_seconds_local -= (self.hours * 3600)
        self.minutes = total_seconds_local // 60
        total_seconds_local -= (self.minutes * 60)
        self.seconds = total_seconds_local
        if self.is_negative == True:
            self.total_seconds = -self.total_seconds
        
    def __repr__(self):
        """ Returns a machine-readable representation of the Duration object
        >>> Duration(1, 45, 45)
        Duration('1:45:45')
        >>> Duration("0d5h8m24s")
        Duration('5:08:24')
        >>> Duration("-0d5h8m24s")
        Duration('-5:08:24')
        """
        if self.is_negative:
            return f"Duration('-{self.hours}:{self.minutes:0>2}:{self.seconds:0>2}')"
        return f"Duration('{self.hours}:{self.minutes:0>2}:{self.seconds:0>2}')"
    
    def __str__(self):
        """ Prints a human-readable representation of the Duration object
        >>> str(Duration(1, 30, 30))
        '1:30:30'
        >>> str(Duration(-1, 30, 30))
        '-1:30:30'
        """
        if self.is_negative:
            return f'-{self.hours}:{self.minutes:0>2}:{self.seconds:0>2}'
        return f'{self.hours}:{self.minutes:0>2}:{self.seconds:0>2}'
        
    def __sub__(self, other):
        """ Subtracts two durations and returns the difference
        >>> Duration(45) - Duration("-45s")
        Duration('0:01:30')
        >>> Duration(59) - Duration("0d0h0m59s")
        Duration('0:00:00')
        """
        return Duration(f"{self.total_seconds - other.total_seconds}s")
    
    def __add__(self, other):
        """ Adds two durations and returns the sum
        >>> Duration(45) + Duration("-45s")
        Duration('0:00:00')
        >>> Duration("0h52m0s") + Duration(0, 9, 0)
        Duration('1:01:00')
        """
        return Duration(f"{self.total_seconds + other.total_seconds}s")
    
    def __mul__(self, multiplier):
        """ Multiplies two durations and returns the product
        >>> str(Duration(45) * (2 * 60))
        '1:30:00'
        >>> str(Duration("30s") * 5)
        '0:02:30'
        """
        return Duration(f"{self.total_seconds * multiplier}s")
    
    def __lt__(self, other):
        """ Determines if a Duration object is less than another
        >>> Duration(45) < Duration(59)
        True
        >>> Duration("1d8h9m52s") < Duration("1d8h9m51s")
        False
        """
        return self.total_seconds < other.total_seconds
    
    def __le__(self, other):
        """ Determines if a Duration object is less than or equal to another
        >>> Duration(45) <= Duration(59)
        True
        >>> Duration("1d8h9m52s") <= Duration("1d8h9m51s")
        False
        """
        return (self < other) or (self == other)
    
    def __gt__(self, other):
        """ Determines if a Duration object is greater than another
        >>> Duration(45) > Duration(59)
        False
        >>> Duration("9d9s") > Duration("9d8s")
        True
        """
        return self.total_seconds > other.total_seconds
    
    def __ge__(self, other):
        """ Determines if a Duration object is greater than or equal to another
        >>> Duration(45) >= Duration(59)
        False
        >>> Duration(300) >= Duration("4m59s")
        True
        """
        return (self > other) or (self == other)
    
    def __eq__(self, other):
        """ Determines if a Duration object is equal to another Duration object
        >>> Duration("1d8h9m52s") == Duration("1d8h9m52s")
        True
        >>> Duration("-30s") == Duration("30s")
        False
        """
        return self.total_seconds == other.total_seconds
    
    def __ne__(self, other):
        """ Determines if a Duration object is not equal to another Duration object
        >>> Duration("5s") != Duration("-5s")
        True
        >>> Duration("1d5m5s") != Duration(24, 5, 5)
        False
        """
        return not (self == other)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()