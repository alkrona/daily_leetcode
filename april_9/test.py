import april_9
from april_9 import timeRequiredToBuy

import unittest
class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = [[2,3,2],2]
        result = timeRequiredToBuy(data[0],data[1])
        self.assertEqual(result,6)
    def test_sample_2(self):
        data = [[5,1,1,1],0]
        result = timeRequiredToBuy(data[0],data[1])
        self.assertEqual(result,8)
    
    
if __name__ == '__main__':
    unittest.main()