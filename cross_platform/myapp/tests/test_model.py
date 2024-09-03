import unittest
from model import Model

class TestModel(unittest.TestCase):
    def test_get_data(self):
        model = Model()
        self.assertEqual(model.get_data(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()