import april_2
from april_2 import isIsomorphic

import unittest

class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = ["egg","add"]
        result = isIsomorphic(data[0],data[1])
        self.assertEqual(result,True)
    def test_sample_2(self):
        data = ["foo","bar"]
        result = isIsomorphic(data[0],data[1])
        self.assertEqual(result,False)
    def test_sample_3(self):
        data = ["paper","title"]
        result = isIsomorphic(data[0],data[1])
        self.assertEqual(result,True)
if __name__ == '__main__':
    unittest.main()