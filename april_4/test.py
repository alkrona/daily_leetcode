import april_4
from april_4 import maxDepth

import unittest
class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = "(1+(2*3)+((8)/4))+1"
        result = maxDepth(data)
        self.assertEqual(result,3)
    def test_sample_1(self):
        data = "(1)+((2))+(((3)))"
        result = maxDepth(data)
        self.assertEqual(result,3)
    
if __name__ == '__main__':
    unittest.main()