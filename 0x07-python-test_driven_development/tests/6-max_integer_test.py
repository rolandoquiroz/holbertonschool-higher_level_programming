#!/usr/bin/python3
""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing
    """
    def test_function(self):
        """Function with all cases
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 2]), 2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-13]), -13)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([1, 3, 8, 2, 6]), 8)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
