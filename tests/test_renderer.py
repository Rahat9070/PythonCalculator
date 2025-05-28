import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from tkinter import ttk
import sys

sys.modules['.Calculator'] = MagicMock()
from src.Render import Render

class TestRender(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.render = Render(master=self.root)
        self.render.calculator = MagicMock()
    
    def tearDown(self):
        self.root.destroy()

    def test_initial_display(self):
        self.assertEqual(self.render.txt_var.get(), "0")
        self.assertEqual(self.render.txt_operator_var.get(), "")

    def test_update_values_calls_calculator_correctly(self):
        self.render.calculator.get_num_string.return_value = "5"
        self.render.calculator.return_num.return_value = 5
        self.render.update_values(5)
        self.render.calculator.add_to_num.assert_called_with(5)
        self.assertEqual(self.render.txt_var.get(), "5")

    def test_update_operator_sets_operator(self):
        self.render.update_operator("+")
        self.assertEqual(self.render.txt_operator_var.get(), "+")
        self.render.calculator.set_operator.assert_called_with("+")

    def test_update_operator_negative_first_number(self):
        self.render.calculator.get_num_string.return_value = ""
        self.render.update_operator("-")
        self.render.calculator.set_subtract_flag.assert_called_with(True)
        self.assertEqual(self.render.txt_var.get(), "-")

    def test_show_answer_success(self):
        self.render.calculator.calculate.return_value = 42
        self.render.show_answer()
        self.assertEqual(self.render.txt_var.get(), "42")
        self.render.calculator.clear_num.assert_called()

    def test_show_answer_error(self):
        self.render.calculator.calculate.side_effect = ValueError("Invalid input")
        self.render.show_answer()
        self.assertEqual(self.render.txt_var.get(), "Invalid input")

    def test_clear_function(self):
        self.render.clear()
        self.render.calculator.clear_function.assert_called()
        self.assertEqual(self.render.txt_var.get(), "0")
        self.assertEqual(self.render.txt_operator_var.get(), "")

if __name__ == '__main__':
    unittest.main()
