"""
Compare two strings by comparing the sum of their values (ASCII character code).
For comparing treat all letters as UpperCase.

Null-Strings should be treated as if they are empty strings.
If the string contains other characters than letters, treat the whole string as it would be empty.

Examples:

"AD","BC" -> equal

"AD","DD" -> not equal

"gf","FG" -> equal

"zz1","" -> equal

"ZzZz", "ffPFF" -> equal

"kl", "lz" -> not equal

null, "" -> equal

Your method should return true, if the strings are equal and false if they are not equal.
"""

def compare(s1,s2):
    sum1 = 0
    sum2 = 0
    try:
        str(s1)
        for ch in s1.upper():
            if not ch.isalpha():
                sum1 = 0
                break
            sum1 += ord(ch)
    except: sum1=0
    try:
        str(s2)
        for ch in s2.upper():
            if not ch.isalpha():
                sum2 = 0
                break
            sum2 += ord(ch)
    except: sum2=0
    if sum1 == sum2:
        return True
    else: return False

if __name__ == '__main__':
    print(compare("AD", "BC"), True, "\'AD\' vs \'BC\'")
    print(compare("AD", "DD"), False, "\'AD\' vs \'DD\'")
    print(compare("gf", "FG"), True, "\'gf\' vs \'FG\'")
    print(compare("Ad", "DD"), False, "\'Ad\' vs \'DD\'")
    print(compare("zz1", ""), True, "\'zz1\' vs \'\'")
    print(compare("ZzZz", "ffPFF"), True, "\'ZzZz\' vs \'ffPFF\'")
    print(compare("kl", "lz"), False, "\'kl\' vs \'lz\'")
    print(compare(None, ""), True, "\'<null>\' vs \'\'")
    print(compare("!!", "7476"), True, "\'!!\' vs \'7476\'")
    print(compare("##", "1176"), True, "\'##\' vs \'1176\'")