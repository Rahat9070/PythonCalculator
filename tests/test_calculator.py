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
    
    def test_add_to_num(self):
        self.calc.add_to_num(5)
        self.assertEqual(self.calc.get_num_string(), "5")
        self.calc.add_to_num(3)
        self.assertEqual(self.calc.get_num_string(), "53")
    
    def test_return_num(self):
        self.calc.add_to_num(5)
        self.assertEqual(self.calc.return_num(), 5)
        self.calc.add_to_num(-3)
        self.assertEqual(self.calc.return_num(), -3)
    
    def test_clear_num(self):
        self.calc.add_to_num(5)
        self.calc.clear_num()
        self.assertEqual(self.calc.get_num_string(), "")
        self.assertEqual(self.calc.return_num(), 5)
    
    def test_clear_stack(self):
        self.calc.add_to_num(5)
        self.calc.clear_num()
        self.calc.clear_stack()
        self.assertEqual(self.calc.stack, [])
    
    def test_set_operator(self):
        self.calc.set_operator('+')
        self.assertEqual(self.calc.operator, '+')
        self.calc.add_to_num(5)
        self.calc.clear_num()
        self.assertEqual(self.calc.get_num_string(), "")
    
    def test_clear_function(self):
        self.calc.add_to_num(5)
        self.calc.set_operator('+')
        self.calc.clear_function()
        self.assertEqual(self.calc.get_num_string(), "")
        self.assertEqual(self.calc.operator, "")
        self.assertFalse(self.calc.subtractFlag)
        self.assertFalse(self.calc.decimalFlag)
    
    def test_set_subtract_flag(self):
        self.calc.set_subtract_flag(True)
        self.assertTrue(self.calc.subtractFlag)
        self.calc.set_subtract_flag(False)
        self.assertFalse(self.calc.subtractFlag)
    
    def test_set_decimal_flag(self):
        self.calc.set_decimal_flag(True)
        self.assertTrue(self.calc.decimalFlag)
        self.calc.set_decimal_flag(False)
        self.assertFalse(self.calc.decimalFlag)
    
    def test_get_num_string(self):
        self.calc.add_to_num(5)
        self.assertEqual(self.calc.get_num_string(), "5")
        self.calc.add_to_num(3)
        self.assertEqual(self.calc.get_num_string(), "53")
        self.calc.clear_num()
        self.assertEqual(self.calc.get_num_string(), "")
    
    def test_get_decimal_flag(self):
        self.calc.set_decimal_flag(True)
        self.assertTrue(self.calc.get_decimal_flag())
        self.calc.set_decimal_flag(False)
        self.assertFalse(self.calc.get_decimal_flag())
    
    def test_get_subtract_flag(self):
        self.calc.set_subtract_flag(True)
        self.assertTrue(self.calc.get_subtract_flag())
        self.calc.set_subtract_flag(False)
        self.assertFalse(self.calc.get_subtract_flag())

if __name__ == '__main__':
    unittest.main()