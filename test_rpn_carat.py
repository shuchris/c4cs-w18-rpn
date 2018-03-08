import unittest
import rpn

class TestCarat(unittest.TestCase):
    def test_carat(self):
        result = rpn.calculate("4 3 ^")
        self.assertEqual(64,result)

