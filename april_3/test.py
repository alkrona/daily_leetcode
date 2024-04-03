import april_3
from april_3 import exist

import unittest
class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"]
        result = exist(data[0],data[1])
        self.assertEqual(result,True)
    def test_sample_1(self):
        data = [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"]
        result = exist(data[0],data[1])
        self.assertEqual(result,True)
    def test_sample_1(self):
        data = [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"]
        result = exist(data[0],data[1])
        self.assertEqual(result,False)
if __name__ == '__main__':
    unittest.main()