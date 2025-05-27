from src.Render import Render
import unittest
from unittest.mock import MagicMock, patch

class TestRender(unittest.TestCase):
    def setUp(self):
        self.render = Render()

    @patch('src.Render.Tk')
    def test_init(self, mock_tk):
        self.assertIsNotNone(self.render.root)
        self.assertIsNotNone(self.render.frm)
        self.assertEqual(self.render.root.title(), "Calculator")

    @patch('src.Render.Tk.mainloop')
    def test_render(self, mock_mainloop):
        self.render.render()
        mock_mainloop.assert_called_once()

    def test_create_textbox(self):
        self.render.create_textbox()
        self.assertEqual(self.render.txt_var.get(), "0")
        self.assertEqual(self.render.txt_operator_var.get(), "")

    def test_create_buttons(self):
        self.render.create_buttons()
        # Check if buttons are created (this is a simple check, more detailed checks can be added)
        self.assertTrue(hasattr(self.render, 'frm'))
        self.assertTrue(hasattr(self.render, 'txt'))


if __name__ == '__main__':
    unittest.main()