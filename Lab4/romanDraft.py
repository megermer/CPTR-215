# Meg Ermer
# CPTR 215 A
# Sources:
    # 
# History:
    # 29 September 2022: Met with Prof O to ask about doctest issue
    # 28 September 2022: I just wrote the whole thing because I was feeling it.

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
    >>> romanFromInt(333)
    'CCCXXXIII'
    >>> romanFromInt(826)
    'DCCCXXVI'
    >>> romanFromInt(99)
    'XCIX'
    """
    romStr = ""
    while num >= 1000:
        num -= 1000
        romStr += 'M'
    while num >= 900:
        num -= 900
        romStr += 'CM'
    while num >= 500:
        num -= 500
        romStr += 'D'
    while num >= 400:
        num -= 400
        romSTr += 'CD'
    while num >= 100:
        num -= 100
        romStr += 'C'
    while num >= 90:
        num -= 90
        romStr += 'XC'
    while num >= 50:
        num -= 50
        romStr += 'L'
    while num >= 40:
        num -= 40
        romStr += 'XL'
    while num >= 10:
        num -= 10
        romStr += 'X'
    while num >= 9:
        num -= 9
        romStr += 'IX'
    while num >= 5:
        num -= 5
        romStr += 'V'
    while num >= 4:
        num -= 4
        romStr += 'IV'
    while num >= 1:
        num -= 1
        romStr += 'I'
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
    
    userInput = input("+-×÷»").split()
    num1 = intFromRoman(userInput[0])
    num2 = intFromRoman(userInput[2])
    if userInput[1] == '+':
        sum = num1 + num2
        print(f"∎QEC: {romanFromInt(sum)}")
    elif userInput[1] == '-':
        difference = num1 - num2
        print(f"∎QEC: {romanFromInt(difference)}")
    elif (userInput[1] == '*') or (userInput[1] == 'x') or (userInput[1] == '∙') or (userInput[1] == '×'):
        product = num1 * num2
        print(f"∎QEC: {romanFromInt(product)}")
    elif (userInput[1] == '/') or (userInput[1] == '÷'):
        quotient = num1 // num2
        print(f"∎QEC: {romanFromInt(quotient)}")

