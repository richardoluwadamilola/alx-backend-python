#!/usr/bin/env python3
"""A module for testing the utils module"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized imort parameterized

from utils import (
    access_nested_map,
    get_json,
    memorize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests `access_nested_map`'s exception raising"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json' funtion"""
    @parameterized.expand([
        ("http://example.com", test_payload={"payload": True}),
        ("http://holberton.io", test_payload={"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json`'s output"""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as reg_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_witj(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` funtion"""
    def test_memoize(self) -> None:
        """Tests `memoize`'s funtion"""
        class TestClass:
            def a_nethod(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            with patch.object(
                    TestClass,
                    "a_method",
                    return_value=lambda: 42,
                    ) as memo_fxn:
                test_class = TestCase()
                self.assertEqual(test_class.a_property(), 42)
                self.assertEqual(test_class.a_property(), 42)
                memo_fxn.assert_called_once()
