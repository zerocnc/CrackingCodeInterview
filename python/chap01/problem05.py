# One Away: There are three types of edits that can be performed on strings: insert a character,
#           remove a character, or replace a character. Given two strings, write a function to
#           check if they are one edit (or zero edits) away.

import unittest

def OneReplace(oldString, newString):
    print("Testing oneAway")

def OneRemove(oldString, newString):
    print("Testing Remove")

def OneInsert(oldString, newString):
    print("Insert")

# My Version Test for all
def OneAway(originalString, newString):
    print("One Away")

    length = len(originalString) - len(newString)

    if (length == 0):
        OneReplace(originalString, newString)
    elif (length == -1):
        OneRemove(originalString, newString)
    elif ( length == 1):
        OneInsert(originalString, newString)
    else :
        print( originalString,newString, "-> false")

class Test(unittest.TestCase):
    dataReplace = [("pale", "bale")]

    def test_Replace(self):
        print("Replace Test")

if __name__ == "__main__":
    unittest.main()