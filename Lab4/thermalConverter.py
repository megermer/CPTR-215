# Meg Ermer
# CPTR 215 A, Lab B
# Sources:
    # For conversion formulas:
        # https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature
# History
    # 22 Sept 2022: Researched conversions, mapped out program on paper, started on main if/else statements, wrote
    #               framework for conversion functions, 


def delisle(temp : float, target : str = 'X') -> float:
    """
    Given a temp to convert, and an (unrequired) target scale, convert the temp to that scale
    :param temp: float
    :param target: str
    :return: float
    >>> delisle(20.0)
    120.0
    >>> delisle(20.0, 'C')
    86.66666666666667
    """
    if target == 'C':
        return 100 - (temp / 3 * 2)
    else:
        return (100 - temp) / 2 * 3

def fahrenheit(temp : float, target : str = 'X') -> float:
    """
    Given a temp to convert, and an (unrequired) target scale, convert the temp to that scale
    :param temp: float
    :param target: str
    :return: float
    >>> fahrenheit(20.0)
    68.0
    >>> fahrenheit(20.0, 'C')
    -6.666666666666666
    """
    if target == 'C':
        return (temp - 32) / 9 * 5
    else: 
        return (temp / 5 * 9) + 32

def kelvin(temp : float, target : str = 'X') -> float:
    """
    Given a temp to convert, and an (unrequired) target scale, convert the temp to that scale
    :param temp: float
    :param target: str
    :return: float
    >>> kelvin(20.0)
    293.15
    >>> kelvin(20.0, 'C')
    -253.14999999999998
    """
    if target == 'C':
        return temp - 273.15
    else: 
        return temp + 273.15

def newton(temp : float, target : str = 'X') -> float:
    """
    Given a temp to convert, and an (unrequired) target scale, convert the temp to that scale
    :param temp: float
    :param target: str
    :return: float
    >>> newton(20.0)
    6.6000000000000005
    >>> newton(20.0, 'C')
    60.60606060606061
    """
    if target == 'C':
        return temp / 33 * 100
    else:
        return temp / 100 * 33

def rankine(temp : float, target : str = 'X') -> float:
    """
    Given a temp to convert, and an (unrequired) target scale, convert the temp to that scale
    :param temp: float
    :param target: str
    :return: float
    >>> rankine(20.0)
    527.6700000000001
    >>> rankine(20.0, 'C')
    -262.0388888888889
    """
    if target == 'C':
        return (temp - 491.67) / 9 * 5
    else:
        return (temp / 5 * 9) + 491.67


def reaumur(temp : float, target : str = 'X') -> float:
    """
    Given a temp to convert, and an (unrequired) target scale, convert the temp to that scale
    :param temp: float
    :param target: str
    :return: float
    >>> reaumur(20.0)
    16.0
    >>> reaumur(20.0, 'C')
    25.0
    """
    if target == 'C':
        return temp * 1.25
    else:
        return temp * 0.8

def romer(temp : float, target : str = 'X') -> float:
    """
    Given a temp to convert, and an (unrequired) target scale, convert the temp to that scale
    :param temp: float
    :param target: str
    :return: float
    >>> romer(20.0)
    18.0
    >>> romer(20.0, 'C')
    23.80952380952381
    """
    if target == 'C':
        return (temp - 7.5) / 21 * 40
    else:
        return (temp / 40 * 21) + 7.5

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    tempToConvert = float(input("Temperature to convert: "))
    startingScale = input("Starting scale (C, D, F, K, N, Ra, Re, Ro): ")
    targetScale = input("Target scale (C, D, F, K, N, Ra, Re, Ro): ")
    convertedTemp = 0
    celsiusTemp = tempToConvert
    if startingScale != 'C':
        if startingScale == 'D':
            celsiusTemp = delisle(tempToConvert, 'C')
        elif startingScale == 'F':
            celsiusTemp = fahrenheit(tempToConvert, 'C')
        elif startingScale == 'K':
            celsiusTemp = kelvin(tempToConvert, 'C')
        elif startingScale == 'N':
            celsiusTemp = newton(tempToConvert, 'C')
        elif startingScale == 'Ra':
            celsiusTemp = rankine(tempToConvert, 'C')
        elif startingScale == 'Re':
            celsiusTemp = reaumur(tempToConvert, 'C')
        elif startingScale == 'Ro':
            celsiusTemp = romer(tempToConvert, 'C')

    if targetScale == 'D':
        convertedTemp = (delisle(celsiusTemp))
    elif targetScale == 'F':
        convertedTemp = (fahrenheit(celsiusTemp))
    elif targetScale == 'K':
        convertedTemp = (kelvin(celsiusTemp))
    elif targetScale == 'N':
        convertedTemp = (newton(celsiusTemp))
    elif targetScale == 'Ra':
        convertedTemp = (rankine(celsiusTemp))
    elif targetScale == 'Re':
        convertedTemp = (reaumur(celsiusTemp))
    elif targetScale == 'Ro':
        convertedTemp = (romer(celsiusTemp))
    elif targetScale == 'C':
        convertedTemp = celsiusTemp
    print()
    print(f"{tempToConvert:.2f}° {startingScale} = {convertedTemp:.2f}° {targetScale}")

