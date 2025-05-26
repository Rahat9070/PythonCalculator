import unittest

from src.Calculator import Calculator

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
    
    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
    
    def test_power_zero(self):
        self.assertEqual(self.calc.power(5, 0), 1)
    
    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)
    
    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_modulus(self):
        self.assertEqual(self.calc.modulus(7, 3), 1)
    
    def test_modulous_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulus(7, 0)

if __name__ == '__main__':
    unittest.main()