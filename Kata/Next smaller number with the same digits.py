"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""

def next_smaller(n):
    num = list(str(n))
    for i in range(len(num)-1, 0, -1):
        if num[i]<num[i-1]:
            lSide = num[:i-1]
            rSide = num[i:]
            c = num[i-1]
            rSide.sort(reverse=True)
            for j in range(len(rSide)):
                if c > rSide[j]:
                    c, rSide[j] = rSide[j], c
                    break
            rSide.sort(reverse=True)
            newNum = lSide + list(c) + rSide
            if newNum[0]=='0':
                return -1
            return int(''.join(newNum))
    return -1
    


if __name__ == "__main__":
    print(next_smaller(907), 790)
    print(next_smaller(531), 513)
    print(next_smaller(135), -1)
    print(next_smaller(2071), 2017)
    print(next_smaller(414), 144)
    print(next_smaller(123456798), 123456789)
    print(next_smaller(123456789), -1)
    print(next_smaller(1234567908), 1234567890)