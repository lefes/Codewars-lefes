"""
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""

def parse(el):
    strukt = []
    try:
        if type(el) == list:
            if len(el)>=1:
                for l in el:
                    strukt.append(parse(l))
                return strukt
            else:
                return [0]
        else:
            return 0
    except:
        return 0

def same_structure_as(original,other):
    return parse(original) == parse(other)



if __name__ == "__main__":
    print(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
    print(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
    print(same_structure_as([1,'[',']'],['[',']',1]), True)
    print(same_structure_as([[[],[]]],[[1,1]]), False)
