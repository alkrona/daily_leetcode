import april_6
from april_6 import minRemoveToMakeValid

import unittest
class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = "lee(t(c)o)de)"
        result = minRemoveToMakeValid(data)
        self.assertEqual(result,"lee(t(c)o)de")
    def test_sample_2(self):
        data = "a)b(c)d"
        result = minRemoveToMakeValid(data)
        self.assertEqual(result,"ab(c)d")
    def test_sample_3(self):
        data = "))(("
        result = minRemoveToMakeValid(data)
        self.assertEqual(result,"")
    
if __name__ == '__main__':
    unittest.main()
