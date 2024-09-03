import unittest
from view import View
from kivy.base import EventLoop

class TestView(unittest.TestCase):
    def setUp(self):
        EventLoop.ensure_window()

    def test_display_data(self):
        view = View()
        view.display_data("Hello, World!")
        self.assertEqual(view.label.text, "Data: Hello, World!")

if __name__ == "__main__":
    unittest.main()