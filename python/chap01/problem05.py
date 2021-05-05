# One Away: There are three types of edits that can be performed on strings: insert a character,
#           remove a character, or replace a character. Given two strings, write a function to
#           check if they are one edit (or zero edits) away.

import unittest

def OneEditAway(oldString, newString):

    if len(oldString) == len(newString) + 1:
        return OneInsert(oldString, newString)
    elif len(oldString) == len(newString) - 1:
        return OneRemove(oldString, newString)
    elif len(oldString) == len(newString):
        return OneReplace(oldString, newString)
    else:
        return False

#   Name: OneReplace
#   Purpose: Checks if one character was replaced.
def OneReplace(oldString, newString):

    for i in range(0, len(oldString)):
        if ( oldString[i] != newString[i] ):
            print( oldString + ", " + newString + " -> " + "false")
            return False

    print( oldString + ", " + newString + " -> " + "true" )
    return True


def OneRemove(oldString, newString):
    pass

def OneInsert(oldString, newString):
    pass

# My Version Test for all
def OneAway(originalString, newString):

    if ( len( originalString) == len(newString)):
        if (OneReplace(originalString, newString)):
            print("Is replace")

class Test(unittest.TestCase):

    def test_OneEditAway(self):
        originalString = ["pale", "pales", "pale", "pale"]
        newString = ["ple", "pale", "bale", "bake"]

        answerKey = [True, True, True, False]

        for ndx in range(4):
            result = OneEditAway(originalString[ndx], newString[ndx])
            self.assertEqual(result, answerKey[ndx])


if __name__ == "__main__":
    unittest.main()