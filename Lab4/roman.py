# Meg Ermer
# CPTR 215 A, Lab B
# Sources:
    # http://home.hiwaay.net/~lkseitz/math/roman/numerals.shtml
        # Used for researching Roman numerals
    # https://catonmat.net/tools/generate-random-roman-numerals
        # Used for generating random Roman numerals that I could use for my tests
# History:
    # 29 September 2022: Met with Prof O, reformatted my romanFromInt to be more
    #                    concise, Brandon helped me fix a debugging issue. I learned not to declare
    #                    variables with the name "sum" when using the sum method in the same program
    # 28 September 2022: I just wrote the whole thing because I was feeling it.

import pdb

romToIntDictIrreg = {
    'I': 1,
    '&': 4,
    'V': 5,
    '?': 9,
    'X': 10,
    '@': 40,
    'L': 50,
    '|': 90,
    'C': 100,
    '~': 400,
    'D': 500,
    '*': 900,
    'M': 1000,
}

intToRomDict = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

def romanFromInt(num: int) -> str:
    """
    Converts a number to its Roman numeral representation in standard form.
    :param num: int
    :return: str
    >>> romanFromInt(3000)
    'MMM'
    >>> romanFromInt(3728)
    'MMMDCCXXVIII'
    >>> romanFromInt(255)
    'CCLV'
    """
    romStr = ""
    pdb.set_trace()
    for value in intToRomDict.keys():
        if num >= value:
            quantity = num // value
            romStr += quantity * (intToRomDict[value])
            num -= quantity * value
    return romStr

def intFromRoman(num: str) -> int:
    """
    Converts a string representing a Roman numeral in standard form to its numeric equivalent
    :param num: str
    :return: int
    >>> intFromRoman('CMVII')
    907
    >>> intFromRoman('CDLXV')
    465
    >>> intFromRoman('XCVI')
    96
    >>> intFromRoman('CCCXLII')
    342
    >>> intFromRoman('CCXIX')
    219
    >>> intFromRoman('DCCXIV')
    714
    """
    intList = []
    if 'CM' in num:
        num = num.replace('CM', '*')
    if 'CD' in num:
        num = num.replace('CD', '~')
    if 'XC' in num:
        num = num.replace('XC', '|')
    if 'XL' in num:
        num = num.replace('XL', '@')
    if 'IX' in num:
        num = num.replace('IX', '?')
    if 'IV' in num:
        num = num.replace('IV', '&')
    for i in range(len(num)):
        # intList.append(romToIntDictIrreg.get(num[i], 'n/a'))
        intList.append(romToIntDictIrreg[num[i]])
    return sum(intList)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    userInput = input("+-×÷» ").split()
    while len(userInput) == 3:
        num1 = intFromRoman(userInput[0])
        num2 = intFromRoman(userInput[2])
        if userInput[1] == '+':
            sum1 = num1 + num2
            print(f"∎QEC: {romanFromInt(sum1)}")
        elif userInput[1] == '-':
            difference = num1 - num2
            print(f"∎QEC: {romanFromInt(difference)}")
        elif (userInput[1] == '*') or (userInput[1] == 'x') or (userInput[1] == '∙') or (userInput[1] == '×'):
            product = num1 * num2
            print(f"∎QEC: {romanFromInt(product)}")
        elif (userInput[1] == '/') or (userInput[1] == '÷'):
            quotient = num1 // num2
            print(f"∎QEC: {romanFromInt(quotient)}")
        userInput = input("+-×÷» ").split()