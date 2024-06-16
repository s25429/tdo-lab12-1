import unittest

from calculator import i_add


class TestCalculatorIntAdd(unittest.TestCase):
    def test_positive_signs(self):
        self.assertEqual(i_add(1, 2), 3)
    
    def test_negative_signs(self):
        self.assertEqual(i_add(-3, -5), -8)
    
    def test_mixed_signs(self):
        self.assertEqual(i_add(-5, 5), 0)
    
    def test_with_zero(self):
        self.assertEqual(i_add(1, 0), 1)


if __name__ == '__main__':
    unittest.main()
