# Meg Ermer
# CPTR 215 A, Lab B
# Sources:
    # Used for researching the names of large numbers:
        # https://www.ibiblio.org/units/large.html
master_string = ""
def isOne(int, master_string):
    """
    Recibe un int y un string y devuelve un string con la palabra para el
    :param int: int
    :param master_string: str
    :return: str

    >>> isOne(9, "")
    'nine'
    >>> isOne(8, "")
    'eight'
    >>> isOne(7, "")
    'seven'
    >>> isOne(6, "")
    'six'
    >>> isOne(5, "")
    'five'
    >>> isOne(4, "")
    'four'
    >>> isOne(3, "")
    'three'
    >>> isOne(2, "")
    'two'
    >>> isOne(1, "")
    'one'
    """
    if int == 9:
        master_string += "nine"
    elif int == 8:
        master_string += "eight"
    elif int == 7:
        master_string += "seven"
    elif int == 6:
        master_string += "six"
    elif int == 5:
        master_string += "five"
    elif int == 4:
        master_string += "four"
    elif int == 3:
        master_string += "three"
    elif int == 2:
        master_string += "two"
    elif int == 1:
        master_string += "one"
    return master_string

def isTen(int, master_string):
    """
    Recibe un int y un string y devuelve un string con la palabra para el
    :param int: int
    :param master_string: str
    :return: str

    >>> isTen(90, "")
    'ninety'
    >>> isTen(80, "")
    'eighty'
    >>> isTen(70, "")
    'seventy'
    >>> isTen(60, "")
    'sixty'
    >>> isTen(50, "")
    'fifty'
    >>> isTen(40, "")
    'forty'
    >>> isTen(30, "")
    'thirty'
    >>> isTen(20, "")
    'twenty'
    >>> isTen(19, "")
    'nineteen'
    >>> isTen(18, "")
    'eighteen'
    >>> isTen(17, "")
    'seventeen'
    >>> isTen(16, "")
    'sixteen'
    >>> isTen(15, "")
    'fifteen'
    >>> isTen(14, "")
    'fourteen'
    >>> isTen(13, "")
    'thirteen'
    >>> isTen(12, "")
    'twelve'
    >>> isTen(11, "")
    'eleven'
    >>> isTen(10, "")
    'ten'
    >>> isTen(31, "")
    'thirty-one'
    """
    if int >= 90:
        master_string += "ninety"
    elif int >= 80:
        master_string += "eighty"
    elif int >= 70:
        master_string += "seventy"
    elif int >= 60:
        master_string += "sixty"
    elif int >= 50:
        master_string += "fifty"
    elif int >= 40:
        master_string += "forty"
    elif int >= 30:
        master_string += "thirty"
    elif int >= 20:
        master_string += "twenty"
    elif int == 19:
        master_string += "nineteen"
    elif int == 18:
        master_string += "eighteen"
    elif int == 17:
        master_string += "seventeen"
    elif int == 16:
        master_string += "sixteen"
    elif int == 15:
        master_string += "fifteen"
    elif int == 14:
        master_string += "fourteen"
    elif int == 13:
        master_string += "thirteen"
    elif int == 12:
        master_string += "twelve"
    elif int == 11:
        master_string += "eleven"
    elif int == 10:
        master_string += "ten"
    if (int >= 20) and (int % 10 != 0):
        master_string += "-"
        return isOne(int % 10, master_string)
    else: 
        return master_string
    
def isHundred(int, master_string):
    """
    Recibe un int y un string y devuelve un string con la palabra para el
    :param int: int
    :param master_string: str
    :return: str

    >>> isHundred(900, "")
    'nine hundred'
    >>> isHundred(800, "")
    'eight hundred'
    >>> isHundred(700, "")
    'seven hundred'
    >>> isHundred(600, "")
    'six hundred'
    >>> isHundred(500, "")
    'five hundred'
    >>> isHundred(400, "")
    'four hundred'
    >>> isHundred(300, "")
    'three hundred'
    >>> isHundred(200, "")
    'two hundred'
    >>> isHundred(100, "")
    'one hundred'
    >>> isHundred(201, "")
    'two hundred one'
    >>> isHundred(832, "")
    'eight hundred thirty-two'
    """
    if int >= 900:
        master_string += "nine hundred"
    elif int >= 800:
        master_string += "eight hundred"
    elif int >= 700:
        master_string += "seven hundred"
    elif int >= 600:
        master_string += "six hundred"
    elif int >= 500:
        master_string += "five hundred"
    elif int >= 400:
        master_string += "four hundred"
    elif int >= 300:
        master_string += "three hundred"
    elif int >= 200:
        master_string += "two hundred"
    elif int >= 100:
        master_string += "one hundred"
    if int % 100 == 0:
        return master_string
    else:
        if master_string[-1] != " ":
            master_string += " "
        if (int % 100 > 0) and (int % 100 < 10):
            return isOne(int % 100, master_string)
        else:
            return isTen(int % 100, master_string)

def isThousand(int, master_string):
    """
    Recibe un int y un string y devuelve/agrega a un string con las palabras para el int
    :param int: int
    :param master_string: str
    :return: str

    >>> isThousand(803267, "")
    'eight hundred three thousand two hundred sixty-seven'
    >>> isThousand(79726, "")
    'seventy-nine thousand seven hundred twenty-six'
    >>> isThousand(1245, "")
    'one thousand two hundred forty-five'
    >>> isThousand(6000, "")
    'six thousand'
    """
    if int // 1000 >= 100:
        master_string += isHundred(int // 1000, master_string) + " thousand"
    elif int // 1000 >= 10:
        master_string += isTen(int // 1000, master_string) + " thousand"
    elif int // 1000 >= 1:
        master_string += isOne(int // 1000, master_string) + " thousand"
    elif int // 1000 == 0:
        return isHundred(int % 1000, master_string)
    if int % 1000 != 0:
        master_string += " "
    return isHundred(int % 1000, master_string)

def isMillion(int, master_string):
    """
    Recibe un int y un string y devuelve/agrega a un string con las palabras para el int

    :param int: int
    :param master_string: str
    :return: str

    >>> isMillion(100835279, "")
    'one hundred million eight hundred thirty-five thousand two hundred seventy-nine'
    >>> isMillion(10738294, "")
    'ten million seven hundred thirty-eight thousand two hundred ninety-four'
    >>> isMillion(1738294, "")
    'one million seven hundred thirty-eight thousand two hundred ninety-four'
    >>> isMillion(2738294, "")
    'two million seven hundred thirty-eight thousand two hundred ninety-four'
    >>> isMillion(2000000, "")
    'two million'
    >>> isMillion(9000000, "")
    'nine million'
    """
    million_string = master_string
    if int // (1 * 10 ** 6) >= 100:
        million_string += isHundred(int // (1 * 10 ** 6), million_string) + " million"
    elif int // (1 * 10 ** 6) >= 10:
        million_string += isTen(int // (1 * 10 ** 6), million_string) + " million"
    elif int // (1 * 10 ** 6) >= 1:
        million_string += isOne(int // (1 * 10 ** 6), million_string) + " million"
    elif int // (1 * 10 ** 6) == 0:
        return million_string + isThousand(int % (1 * 10 ** 6), master_string)
    if int % (1 * 10 ** 6) != 0:
        million_string += " "
    return million_string + isThousand(int % (1 * 10 ** 6), master_string)

def isBillion(int, master_string):
    """
    Recibe un int y un string y devuelve/agrega a un string con las palabras para el int
    :param int: int
    :param master_string: str
    :return: str

    >>> isBillion(938847362817, "")
    'nine hundred thirty-eight billion eight hundred forty-seven million three hundred sixty-two thousand eight hundred seventeen'
    >>> isBillion(46728635901, "")
    'forty-six billion seven hundred twenty-eight million six hundred thirty-five thousand nine hundred one'
    >>> isBillion(2364829563, "")
    'two billion three hundred sixty-four million eight hundred twenty-nine thousand five hundred sixty-three'
    >>> isBillion(1000000000, "")
    'one billion'
    """
    billion_string = master_string
    if int // (1 * 10 ** 9) >= 100:
        billion_string += isHundred(int // (1 * 10 ** 9), billion_string) + " billion"
    elif int // (1 * 10 ** 9) >= 10:
        billion_string += isTen(int // (1 * 10 ** 9), billion_string) + " billion"
    elif int // (1 * 10 ** 9) >= 1:
        billion_string += isOne(int // (1 * 10 ** 9), billion_string) + " billion"
    elif int // (1 * 10 ** 9) == 0:
        return billion_string + isMillion(int % (1 * 10 ** 9), master_string)
    if int % (1 * 10 ** 9) != 0:
        billion_string += " "   
    return billion_string + isMillion(int % (1 * 10 ** 9), master_string)

def isTrillion(int, master_string):
    """
    Recibe un int y un string y devuelve/anada a un string con las palabras para el int 
    :param int: int
    :param master_string: str
    :return: str
    
    >>> isTrillion(753758492089462, "")
    'seven hundred fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isTrillion(53758492089462, "")
    'fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isTrillion(3758492089462, "")
    'three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isTrillion(7907896543174, "")
    'seven trillion nine hundred seven billion eight hundred ninety-six million five hundred forty-three thousand one hundred seventy-four'
    >>> isTrillion(1000000000000, "")
    'one trillion'
    """
    trillion_string = master_string
    if int // (1 * 10 ** 12) >= 100:
        trillion_string += isHundred(int // (1 * 10 ** 12), trillion_string) + " trillion"
    elif int // (1 * 10 ** 12) >= 10:
        trillion_string += isTen(int // (1 * 10 ** 12), trillion_string) + " trillion"
    elif int // (1 * 10 ** 12) >= 1:
        trillion_string += isOne(int // (1 * 10 ** 12), trillion_string) + " trillion"
    elif int // (1 * 10 ** 12) == 0:
        return trillion_string + isBillion(int % (1 * 10 ** 12), master_string)
    if int % (1 * 10 ** 12) != 0:
        trillion_string += " "
    return trillion_string + isBillion(int % (1 * 10 ** 12), master_string)

def isQuadrillion(int, master_string):
    """
    Recibe un int y un string y devuelve/anada a un string con las palabras para el int 
    :param int: int
    :param master_string: str
    :return: str

    >>> isQuadrillion(302753758492089462, "")
    'three hundred two quadrillion seven hundred fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isQuadrillion(22753758492089462, "")
    'twenty-two quadrillion seven hundred fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isQuadrillion(2753758492089462, "")
    'two quadrillion seven hundred fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isQuadrillion(2000000000000000, "")
    'two quadrillion'
    """
    quadrillion_string = master_string
    if int // (1 * 10 ** 15) >= 100:
        quadrillion_string += isHundred(int // (1 * 10 ** 15), quadrillion_string) + " quadrillion"
    elif int // (1 * 10 ** 15) >= 10:
        quadrillion_string += isTen(int // (1 * 10 ** 15), quadrillion_string) + " quadrillion"
    elif int // (1 * 10 ** 15) >= 1:
        quadrillion_string += isOne(int // (1 * 10 ** 15), quadrillion_string) + " quadrillion"
    #ADDED ELIF BELOW
    elif int // (1 * 10 ** 15) == 0:
        return quadrillion_string + isTrillion(int % (1 * 10 ** 15), master_string)
    if int % (1 * 10 ** 15) != 0:
        quadrillion_string += " "
    return quadrillion_string + isTrillion(int % (1 * 10 ** 15), master_string)

def isQuintillion(int, master_string):
    """
    Recibe un int y un string y devuelve/anada a un string con las palabras para el int
    :param int: int
    :param master_string: str
    :return: str  

    >>> isQuintillion(967302753758492089462, "")
    'nine hundred sixty-seven quintillion three hundred two quadrillion seven hundred fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isQuintillion(67302753758492089462, "")
    'sixty-seven quintillion three hundred two quadrillion seven hundred fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isQuintillion(7302753758492089462, "")
    'seven quintillion three hundred two quadrillion seven hundred fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> isQuintillion(6000000000000000000, "")
    'six quintillion'
    """
    quintillion_string = master_string
    if int // (1 * 10 ** 18) >= 100:
        quintillion_string += isHundred(int // (1 * 10 ** 18), quintillion_string) + " quintillion"
    elif int // (1 * 10 ** 18) >= 10:
        quintillion_string += isTen(int // (1 * 10 ** 18), quintillion_string) + " quintillion"
    elif int // (1 * 10 ** 18) >= 1:
        quintillion_string += isOne(int // (1 * 10 ** 18), quintillion_string) + " quintillion"
    elif int // (1 * 10 ** 18) == 0:
        return quintillion_string + isQuadrillion(int % (1 * 10 ** 18), master_string)
    if int % (1 * 10 ** 18) != 0:
        quintillion_string += " "
    return quintillion_string + isQuadrillion(int % (1 * 10 ** 18), master_string)

def wordsFromNumber(number):
    """
    Given a digit number, return the word name for it

    :param number: str
    :return: str
    >>> wordsFromNumber(0)
    'zero'
    >>> wordsFromNumber(1)
    'one'
    >>> wordsFromNumber(10)
    'ten'
    >>> wordsFromNumber(23)
    'twenty-three'
    >>> wordsFromNumber(20)
    'twenty'
    >>> wordsFromNumber(18)
    'eighteen'
    >>> wordsFromNumber(45)
    'forty-five'
    >>> wordsFromNumber(99)
    'ninety-nine'
    >>> wordsFromNumber(324)
    'three hundred twenty-four'
    >>> wordsFromNumber(404)
    'four hundred four'
    >>> wordsFromNumber(592)
    'five hundred ninety-two'
    >>> wordsFromNumber(892)
    'eight hundred ninety-two'
    >>> wordsFromNumber(1000)
    'one thousand'
    >>> wordsFromNumber(3245)
    'three thousand two hundred forty-five'
    >>> wordsFromNumber(3200)
    'three thousand two hundred'
    >>> wordsFromNumber(4005)
    'four thousand five'
    >>> wordsFromNumber(10324)
    'ten thousand three hundred twenty-four'
    >>> wordsFromNumber(50000)
    'fifty thousand'
    >>> wordsFromNumber(367829)
    'three hundred sixty-seven thousand eight hundred twenty-nine'
    >>> wordsFromNumber(1000000)
    'one million'
    >>> wordsFromNumber(10000000)
    'ten million'
    >>> wordsFromNumber(1738294)
    'one million seven hundred thirty-eight thousand two hundred ninety-four'
    >>> wordsFromNumber(938847362817)
    'nine hundred thirty-eight billion eight hundred forty-seven million three hundred sixty-two thousand eight hundred seventeen'
    >>> wordsFromNumber(3758492089462)
    'three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> wordsFromNumber(22753758492089462)
    'twenty-two quadrillion seven hundred fifty-three trillion seven hundred fifty-eight billion four hundred ninety-two million eighty-nine thousand four hundred sixty-two'
    >>> wordsFromNumber(7736295738017482963)
    'seven quintillion seven hundred thirty-six quadrillion two hundred ninety-five trillion seven hundred thirty-eight billion seventeen million four hundred eighty-two thousand nine hundred sixty-three'
    >>> wordsFromNumber(8826221000655595414)
    'eight quintillion eight hundred twenty-six quadrillion two hundred twenty-one trillion six hundred fifty-five million five hundred ninety-five thousand four hundred fourteen'
    >>> wordsFromNumber(8000382)
    'eight million three hundred eighty-two'
    >>> wordsFromNumber(304000786726463749032)
    'three hundred four quintillion seven hundred eighty-six trillion seven hundred twenty-six billion four hundred sixty-three million seven hundred forty-nine thousand thirty-two'
    """
    num_string = str(number)
    num_int = int(number)
    if num_int == 0:
        return "zero"
    elif len(num_string) >= 19:
        return isQuintillion(num_int, master_string)
    elif len(num_string) >= 16:
        return isQuadrillion(num_int, master_string)
    elif len(num_string) >= 13:
        return isTrillion(num_int, master_string)
    elif len(num_string) >= 10:
        return isBillion(num_int, master_string)
    elif len(num_string) >= 7:
        return isMillion(num_int, master_string)
    elif len(num_string) >= 4:
        return isThousand(num_int, master_string)
    elif len(num_string) >= 3:
        return isHundred(num_int, master_string)
    elif len(num_string) >= 2:
        return isTen(num_int, master_string)
    elif len(num_string) == 1:
        return isOne(num_int, master_string)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)