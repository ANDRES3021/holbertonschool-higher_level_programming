#!/usr/bin/python3
"""Unittest  max_integer([..])
"""
import unittest


max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class unittest for max_integer
    """

    def test_return(self):
        """
        Check return function
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_difference(self):
        """
        Check difference value
        """
        self.assertNotEqual(max_integer([1, 2, 3, 4]), 8)

    def test_empty(self):
        """
        Check list is empty
        """
        result = max_integer()
        self.assertIsNone(result)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer(([1, "s", 3, 4]), 4)

    def test_Equal_string(self):
        """
        Check result is 0
        """
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_tuple(self):
        """
        Check value tuple
        """
        self.assertEqual(max_integer((5, 10)), 10)

    def test_float(self):
        """
        Check result float
        """
        self.assertEqual(max_integer([2, 9.3, 6]), 9.3)

    def test_float(self):
        """Check argument is a list"""
        with self.assertRaises(TypeError):
            max_integer(15)

    def test_sum_t(self):
        """Check sum Arguments"""
        self.assertEqual(max_integer([10 + 10, 20]), 20)


if __name__ == "__main__":
    unittest.main()
