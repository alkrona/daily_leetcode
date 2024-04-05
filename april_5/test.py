import april_5
from april_5 import makeGood

import unittest
class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = "leEeetcode"
        result = makeGood(data)
        self.assertEqual(result,"leetcode")
    def test_sample_2(self):
        data = "abBAcC"
        result = makeGood(data)
        self.assertEqual(result,"")
    def test_sample_3(self):
        data = "s"
        result = makeGood(data)
        self.assertEqual(result,"s")
    
if __name__ == '__main__':
    unittest.main()