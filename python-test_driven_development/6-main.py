#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	def test_max_integer(self):
		self.assertEqual(max_integer([1, 2, 3, 4]), 4)
		self.assertEqual(max_integer([1, 3, 4, 2]), 4)
		self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
		self.assertEqual(max_integer([4]), 4)
		self.assertEqual(max_integer([]), None)
		self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
		
	def test_empty_list(self):
		self.assertIsNone(max_integer([]))
	
	def test_negative_numbers(self):
		self.assertEqual(max_integer([-1, -2, -3]), -1)
		
	def test_same_numbers(self):
		self.assertEqual(max_integer([5, 5, 5, 5]), 5)
    