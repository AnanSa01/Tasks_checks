import unittest

from unitttest.math_function import is_even, sum_function, is_odd, div_function, sub_function, mul_function


class TestMatchFunction(unittest.TestCase):

    def test_is_even_true(self):
        num = 4
        # change arguments here
        result = is_even(num)
        self.assertTrue(result)

    def test_is_even_false(self):
        num = 3
        # change arguments here
        result = is_even(num)
        self.assertFalse(result)

    def test_is_odd_true(self):
        num = 7
        # change arguments here
        result = is_odd(num)
        self.assertTrue(result)

    def test_is_odd_false(self):
        num = 8
        # change arguments here
        result = is_odd(num)
        self.assertFalse(result)

    def test_sum_true(self):
        num1 = 3
        num2 = 6
        # change arguments here
        self.assertEqual(num1+num2, sum_function(num1,num2),"The result is false")

    def test_sub_true(self):
        num1 = 20
        num2 = 12
        # change arguments here
        self.assertEqual(num1 - num2, sub_function(num1, num2), "The result is false")

    def test_mul_true(self):
        num1 = 7
        num2 = 5
        # change arguments here
        self.assertEqual(num1 * num2, mul_function(num1, num2), "The result is false")

    def test_div_true(self):
        num1 = 9
        num2 = 0
        # change arguments here
        try:
            self.assertEqual(num1 / num2, div_function(num1, num2), "The result is false")

        except ZeroDivisionError:
            print("\nnum2 can't be zero")


    def test_modulo_true(self):
        num1 = 5
        # change arguments here.
        self.assertEqual(0,num1,"The result is false")
