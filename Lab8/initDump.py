__init__ dump

def __init__(self, param1, param2 = None, param3 = None):
        """
        >>> Duration(23, 59, 59)
        Duration('23:59:59')
        >>> Duration(2)
        Duration('0:00:02')
        >>> Duration(75)
        Duration('0:01:15')
        >>> Duration("1:30:00")
        Duration('1:30:00')
        >>> Duration("0d0h45s")
        Duration('0:00:45')
        >>> Duration("-45s")
        Duration('-0:00:45')
        >>> Duration('-0:00:45')
        Duration('-0:00:45')
        >>> str(Duration('0:00:45'))
        'Duration('0:00:45')'
        """
        self.isNegative = False  
        # FIELDS: days, hours, minutes, seconds, total_seconds

        if type(param1) == int: # For cases with ints:
            if param1 < 0:
                self.isNegative = True
                param1 = -param1
            if type(param2) == int: # For cases in form (hr, min, sec)
                self.total_seconds = (param1 * 3600) + (param2 * 60) + (param3)
            else: # For cases that have (sec)
                self.total_seconds = param1
                
        if type(param1) == str: # For cases with strings:
            if param1[0] == "-":
                self.isNegative = True
                param1 = param1[1:]
            if ":" in param1: # For cases in form ("hr:min:sec")
                param1_list = param1.split(":")
                self.total_seconds = (int(param1_list[0]) * 3600) + (int(param1_list[1]) * 60) + (int(param1_list[2]))
            else:
                self.total_seconds = 0
                string = param1
                if "d" in string:
                    d_index = string.index("d")
                    self.total_seconds += int(string[0:d_index]) * 86400
                    string = string[d_index+1:]
                if "h" in string:
                    h_index = string.index("h")
                    self.total_seconds += int(string[0:h_index]) * 3600
                    string = string[h_index+1:]
                if "m" in string:
                    m_index = string.index("m")
                    self.total_seconds += int(string[0:m_index]) * 60
                    string = string[m_index+1:]
                if "s" in string:
                    s_index = string.index("s")
                    self.total_seconds += int(string[0:s_index])       
        # Calculates the hours, minutes, and seconds from total_seconds
        total_seconds_local = self.total_seconds
        self.hours = total_seconds_local // 3600
        total_seconds_local -= (self.hours * 3600)
        self.minutes = total_seconds_local // 60
        total_seconds_local -= (self.minutes * 60)
        self.seconds = total_seconds_local