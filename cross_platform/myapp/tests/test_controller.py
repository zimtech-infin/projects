import unittest
from model import Model
from view import View
from controller import Controller
from kivy.base import EventLoop

class TestController(unittest.TestCase):
    def setUp(self):
        EventLoop.ensure_window()

    def test_update_view(self):
        model = Model()
        view = View()
        controller = Controller(model, view)
        controller.update_view()
        self.assertEqual(view.label.text, "Data: Hello, World!")

if __name__ == "__main__":
    unittest.main()