
import unittest
from mathexercise import add

class TestAddFunction(unittest.TestCase):
    # TODO:
    # - Write tests for:
    #   * adding two positive numbers
    #   * adding two negative numbers
    #   * adding a positive and a negative number
    # - Use assertEqual to check the results.
    # - Use clear method names, e.g. test_add_positive_numbers, etc.

    # write your tests here:
    def test_add_two_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_two_negative_numbers(self):
        self.assertEqual(add(-4, -6), -10)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 5), 4)

if __name__ == "__main__":
    unittest.main()