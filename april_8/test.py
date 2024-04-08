import april_8
from april_8 import countStudents

import unittest
class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = [[1,1,0,0],[0,1,0,1]]
        result = countStudents(data[0],data[1])
        self.assertEqual(result,0)
    def test_sample_2(self):
        data = [[1,1,1,0,0,1],[1,0,0,0,1,1]]
        result = countStudents(data[0],data[1])
        self.assertEqual(result,3)
    
    
if __name__ == '__main__':
    unittest.main()