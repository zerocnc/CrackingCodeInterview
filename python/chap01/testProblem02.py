import unittest
import problem02

class TestProblem02(unittest.TestCase):

    def test_IsPermutation(self):
        self.assertEqual( problem02.IsPermutation("x","x") , True )
        self.assertEqual( problem02.IsPermutation("x","xb") , False )
        self.assertEqual( problem02.IsPermutation("abc","cba") , True )
        self.assertEqual( problem02.IsPermutation("abc","cbad") , False )
        self.assertEqual( problem02.IsPermutation("cbad","abc") , False )
        self.assertEqual( problem02.IsPermutation("xxx","xxx") , True )

if __name__ == '__main__':
    unittest.main()