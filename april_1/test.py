import april_1


import unittest

class TestString(unittest.TestCase):
    def test_sample_1(self):
        data = "Hello World"
        result = april_1.lengthOfLastWord(data)
        self.assertEqual(result,5)
    def test_sample_2(self):
        data = "   fly me   to   the moon  "
        result = april_1.lengthOfLastWord(data)
        self.assertEqual(result,4)
    def test_sample_3(self):
        data = "luffy is still joyboy"
        result = april_1.lengthOfLastWord(data)
        self.assertEqual(result,6)
if __name__ == '__main__':
    unittest.main()