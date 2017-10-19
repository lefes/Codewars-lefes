"""
Write function scramble(str1,str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
"""

def scramble(s1,s2):
    alfavit = 'abcdefghijklmnopqrstuvwxyz'
    str1_az = {a: 0 for a in alfavit}
    str2_az = {a: 0 for a in alfavit}
    result = {a: 0 for a in alfavit}
    for char in s1:
        str1_az[char] += 1
    for char in s2:
        str2_az[char] += 1
    for char in alfavit:
        result[char] = str2_az[char] - str1_az[char]
    for char in alfavit:
        if result[char] > 0: return False
    return True

if __name__ == '__main__':
    print(scramble('rkqodlw', 'wworld'), "True")
    print(scramble('cedewaraaossoqqyt', 'codewars'), True)
    print(scramble('katas', 'steak'), False)
    print(scramble('scriptjava', 'javascript'), True)
    print(scramble('scriptingjava', 'javascript'), True)