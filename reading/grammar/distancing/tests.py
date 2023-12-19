import unittest

from distancing import token_range

class TestSum(unittest.TestCase):
    def test(self):
        """
        test of basic sentence
        """
        data = ["the", "quick", "brown", "fox", "jumped", "over", 'the', 'lazy', 'dog.', 'great', 'fucking', 'fox!']
        result = token_range(3, data, 2, 3, ['the'])
        self.assertEqual(result, [('quick', 2), ('brown', 1), ('fox', 0), ('jumped', 1), ('over', 2), ('lazy', 4)])

if __name__ == '__main__':
    unittest.main()
