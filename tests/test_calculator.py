import unittest

from ..src.Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
    
    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_modulus(self):
        self.assertEqual(self.calc.modulus(10, 3), 1)
        with self.assertRaises(ValueError):
            self.calc.modulus(10, 0)
    
    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        with self.assertRaises(ValueError):
            self.calc.divide(-10, 0)