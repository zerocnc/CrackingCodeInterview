# Check Permutation: given two strings, write a method to decide if one is a permuation of the other.

def IsPermutation(strVal1, strVal2):
    dict = {}

    # If the lengths don't match, it's not a permutation
    if len(strVal1) != len(strVal2) :
        return False
    elif len(strVal1) == 0 and len(strVal2) == 0:
        return True

    for char in strVal1:
        if char in dict:
            dict[char]+= 1
        else:
            dict[char] = 1

    for char in strVal2:
        if char in dict:
            dict[char]-= 1
        else:
            return False

    for char in dict:
        if dict[char] > 0:
            return False
        
    return True