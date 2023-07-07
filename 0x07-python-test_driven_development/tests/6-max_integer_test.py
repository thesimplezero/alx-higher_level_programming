#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def setUp(self):
        """ Set up test variables."""
        self.tests = {
            'ordered': ([1, 2, 3, 4], 4),
            'unordered': ([1, 2, 4, 3], 4),
            'max_at_beginning': ([4, 3, 2, 1], 4),
            'empty': ([], None),
            'one_element': ([7], 7),
            'floats': ([1.53, 6.33, -9.123, 15.2, 6.0], 15.2),
            'ints_and_floats': ([1.53, 15.5, -9, 15, 6], 15.5),
            'string': ("Brennan", 'r'),
            'strings': (["Brennan", "is", "my", "name"], "name"),
            'empty_string': ("", None)
        }

    def test_max_integer(self):
        """Perform the tests."""
        for key in self.tests:
            with self.subTest(key=key):
                self.assertEqual(max_integer(self.tests[key][0]), self.tests[key][1])

if __name__ == '__main__':
    unittest.main()
