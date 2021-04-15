# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a 
# palindrome. A palindrome is a word or prhase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. THe palindrome does not need to be limited to just dictionary words.

import unittest

# My Version
def IsPalAPer(string):

    # Create character array.
    char_set = []
    char_set = [ 0 for _ in range(128)]

    # Storing array
    for char in string:
        val = ord(char)

        if char_set[val]:
            char_set[val]+=1
        else:
            char_set[val]==1

    countOdds = 0

    for char in char_set:
        if ( char % 2 != 0):
            countOdds += 1
            if countOdds > 1:
                return False
    
    return True

class Test(unittest.TestCase):
    dataT = [("Tact Coa"), ("jhsabckuj ahjsbckj"), ("Able was I ere I saw Elb")]
    dataF = [("Test No")]

    def test_permuation(self):
        # True check
        print("True Check")
        for test_string in self.dataT:
            actual = IsPalAPer(test_string)
            print(test_string)
            self.assertTrue(actual)

        # True check
        for test_string in self.dataF:
            actual = IsPalAPer(test_string)
            self.assertTrue(actual)

if __name__ == "__main__":
    unittest.main()