#!/usr/bin/python3
"""Unittest  max_integer([..])
"""
import unittest


max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class unittest for max_integer
    """

    def return_test(self):
        """
        Check return function
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def difference_test(self):
        """
        Check difference value
        """
        self.assertNotEqual(max_integer([1, 2, 3, 4]), 8)

    def empty_test(self):
        """
        Check list is empty
        """
        result = max_integer()
        self.assertIsNone(result)

    def string_test(self):
        with self.assertRaises(TypeError):
            max_integer(([1, "s", 3, 4]), 4)

    def Equal_string_test(self):
        """
        Check result is 0
        """
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def tuple_test(self):
        """
        Check value tuple
        """
        self.assertEqual(max_integer((5, 10)), 10)

    def float_test(self):
        """
        Check result float
        """
        self.assertEqual(max_integer([2, 9.3, 6]), 9.3)

    def argument_test(self):
        """Check argument is a list"""
        with self.assertRaises(TypeError):
            max_integer(15)

    def sum_test(self):
        """Check sum Arguments"""
        self.assertEqual(max_integer([10 + 10, 20]), 20)


if __name__ == "__main__":
    unittest.main()