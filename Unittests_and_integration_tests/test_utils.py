#!/usr/bin/env python3
"""Test Utils File"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Test Access Nested Map Class"""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """Test Access Nested Map Method"""
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)
