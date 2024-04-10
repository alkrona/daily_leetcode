import april_10
from april_10 import deckRevealedIncreasing

import unittest
class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = [1,1000]
        result = deckRevealedIncreasing(data)
        self.assertEqual(result,[1,1000])
    def test_sample_2(self):
        data = [17,13,11,2,3,5,7]
        result = deckRevealedIncreasing(data)
        self.assertEqual(result,[2,13,3,11,5,17,7])
    
    
if __name__ == '__main__':
    unittest.main()