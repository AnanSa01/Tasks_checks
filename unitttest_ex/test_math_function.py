import unittest

from math_function import is_even, is_odd


class TestMatchFunction(unittest.TestCase):

# ----------------------------------------------------------
    # checks for even function
    def test_is_even_true(self):
        list_num = [-4, 0, 2]
        # change arguments here
        for num in list_num:
            self.assertTrue(is_even(num))

    def test_is_even_false(self):
        list_num = [-7, 1, 13]
        # change arguments here
        for num in list_num:
            self.assertFalse(is_even(num))

    def test_is_even_float(self):
        list_num_float = [-8.9, 0.6, 16.4]
        # change arguments here
        for num in list_num_float:
            self.assertFalse(is_even(num))

    def test_is_even_str(self):
        list_str = ["aaa", "123", "@#$"]
        for check in list_str:
            with self.assertRaises(TypeError):
                is_even(check)
# ----------------------------------------------------------
    # checks for odd function

    def test_is_odd_true(self):
        list_num = [-7, 1, 13]
        # change arguments here
        for num in list_num:
            self.assertTrue(is_odd(num))

    def test_is_odd_false(self):
        list_num = [-4, 0, 2]
        # change arguments here
        for num in list_num:
            self.assertFalse(is_odd(num))

    def test_is_odd_float(self):
        list_num_float = [-8.9, 0.6, 16.4]
        # change arguments here
        for num in list_num_float:
            self.assertFalse(is_odd(num))

    def test_is_odd_str(self):
        list_str = ["aaa", "123", "@#$"]
        for check in list_str:
            with self.assertRaises(TypeError):
                is_odd(check)
#.
