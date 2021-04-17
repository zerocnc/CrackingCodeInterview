# One Away: There are three types of edits that can be performed on strings: insert a character,
#           remove a character, or replace a character. Given two strings, write a function to
#           check if they are one edit (or zero edits) away.

import unittest

def OneReplace(oldString, newString):
    print("Testing Replace")
    flag = True

    for i in range(0, len(oldString)):
        if ( oldString[i] != newString[i] ):
            print( oldString + ", " + newString + " -> " + "false")
            return False

    print( oldString + ", " + newString + " -> " + "true" )
    return True


def OneRemove(oldString, newString):
    print("Testing Remove")

def OneInsert(oldString, newString):
    print("Testing Insert")

# My Version Test for all
def OneAway(originalString, newString):

    if ( len( originalString) == len(newString)):
        if (OneReplace(originalString, newString)):
            print("Is replace")

class Test(unittest.TestCase):
    dataOriginal = ["pale"]
    dataNew = ["bale"]

    def test_OneAway(self):
        OneAway("pale", "bale")

if __name__ == "__main__":
    unittest.main()