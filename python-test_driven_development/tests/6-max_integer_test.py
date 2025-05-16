#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for testing max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_identical_values(self):
        """Test with identical values"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_strings(self):
        """Test with strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer("abc"), "c")
        self.assertEqual(max_integer(""), None)

    def test_mixed_list(self):
        """Test with list containing mixed types will cause TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

    def test_none_argument(self):
        """Test with None as argument will cause TypeError"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_not_list(self):
        """Test with non-iterable argument will cause TypeError"""
        with self.assertRaises(TypeError):
            max_integer(123)


if __name__ == '__main__':
    unittest.main()
