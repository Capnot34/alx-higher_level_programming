#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """Testing normal lists"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)
    
    def test_edge_cases(self):
        """Testing edge cases"""
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_invalid_inputs(self):
        """Testing invalid inputs"""
        with self.assertRaises(TypeError):
            max_integer(123)
            max_integer("string")
            max_integer([1, "string", 3, 4])
            max_integer((1, 2, 3, 4))
