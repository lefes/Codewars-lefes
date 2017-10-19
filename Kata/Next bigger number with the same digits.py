"""
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
"""

def next_bigger(n):
    string = str(n)
    rslt = ''
    for num in range(len(string)-1, 0, -1):
        if string[num] > string[num-1]:
            tmp = string[num:]
            temp = list(tmp)
            temp.sort()
            for i in temp:
                if int(string[num-1]) < int(i):
                    number = i
                    break
            tmp = tmp.replace(number, '', 1)
            tmp += string[num-1]
            temp = list(tmp)
            temp.sort()
            rslt = string[:num-1] + number + ''.join(temp)
            return int(rslt)
    if not rslt: return -1


if __name__ == '__main__':
    print(next_bigger(2017),2071)
    print(next_bigger(12),21)
    print(next_bigger(513),531)
    print(next_bigger(414),441)
    print(next_bigger(144),414)