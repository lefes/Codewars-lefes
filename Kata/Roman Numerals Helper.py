"""
Create a RomanNumerals helper that can convert a roman numeral to and from an integer value. The class should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Examples:

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
"""

class RomanNumerals():
    @staticmethod
    def to_roman(digit):
        digit_dict = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',
                                10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',
                                100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
                                1000:'M', 2000:'MM', 3000:'MMM'}

        digits = []
        romans = []
        for num, dig in enumerate(list(str(digit))[::-1]):
            digits.append(int(dig)*10**num)
        for ch in digits[::-1]:
            romans.append(digit_dict.get(ch))
        return ''.join(romans)

    @staticmethod
    def from_roman(symvol):
        roman_dict = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9,
                                'X':10, 'XX':20, 'XXX':30, 'XL':40, 'L':50, 'LX':60, 'LXX':70, 'LXXX':80, 'XC':90,
                                'C':100, 'CC':200, 'CCC':300, 'CD':400, 'D':500, 'DC':600, 'DCC':700, 'DCCC':800, 'CM':900,
                                'M':1000, 'MM':2000, 'MMM':3000}
        romans = ['MMM', 'MM', 'M', 'CM', 'DCCC', 'DCC', 'DC', 'CD', 'D', 'CCC', 'CC', 'XC', 'C', 'LXXX', 'LXX', 'LX', 'XL', 'L', 'XXX', 'XX', 'IX', 'X', 'VIII', 'VII', 'VI', 'IV', 'V', 'III', 'II', 'I']
        result = 0
        for ch in romans:
            if symvol.find(ch) != -1:
                symvol = symvol.replace(ch, '')
                result += roman_dict.get(ch)
        return result

if __name__ == '__main__':
    print(RomanNumerals.from_roman('M'), 1000)
    print(RomanNumerals.to_roman(1000), 'M')
    print(RomanNumerals.to_roman(1666), 'MDCLXVI')
    print(RomanNumerals.from_roman('MDCLXVI'), 1666)
    print(RomanNumerals.from_roman('IV'), 4)