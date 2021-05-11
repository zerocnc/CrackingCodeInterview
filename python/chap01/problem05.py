# One Away: There are three types of edits that can be performed on strings: insert a character,
#           remove a character, or replace a character. Given two strings, write a function to
#           check if they are one edit (or zero edits) away.

import unittest

def OneEditAway(oldString, newString):

    if len(oldString) == len(newString):
        return OneReplace(oldString, newString)
    elif len(oldString) - 1 == len(newString):
        return OneRemove(oldString, newString)
    elif len(oldString) + 1 == len(newString):
        return OneReplace(oldString, newString)
    else:
        return False

#   Name: OneReplace
#   Purpose: Checks if one character was replaced.
def OneReplace(oldString, newString):

    foundDifference = False

    for i in range(len(oldString)):
        if(oldString[i] != newString[i]):
            if(foundDifference):
                return False
            foundDifference = True

    return True


def OneRemove(oldString, newString):
    tempPos_X = 0
    tempPos_Y = 0
    flag = True

    for i in range(len(newString)):
        if oldString[tempPos_X] != newString[tempPos_Y] or flag:
            continue
        else:
            return False
        
        tempPos_Y += 1

    return True

def OneInsert(oldString, newString):
    index1 = 0
    index2 = 0

    while(index2 < len(newString) and index1 < len(oldString)):
        if(oldString[index1] != newString[index2]):
            if (index1 != index2):
                return False
            index2 += 1
        else:
            index1+=1
            index2+=1

    return True

class Test(unittest.TestCase):
    originalString = ["pale", "pales", "pale", "pale"]
    newString = ["ple", "pale", "bale", "bake"]

    answerKey = [True, True, True, False]

    def test_OneRemove(self):
        self.assertTrue(OneRemove("pale", "ple"))

    def test_OneInsert(self):
        self.assertTrue(OneInsert("pale", "pales"))
    
    def test_OneReplace(self):
        self.assertTrue(OneReplace("pale", "bale"))

if __name__ == "__main__":
    unittest.main()