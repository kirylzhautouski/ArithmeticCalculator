import unittest
import random

from unittest.mock import MagicMock

from calculator import Calc


class TestCalcCase(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calc()

    def tearDown(self):
        self.calc = None


class TestCalcAdd(TestCalcCase):

    def test_add_two_positives(self):
        self.assertEqual(self.calc.add(20, 35), 55)

    def test_add_two_positives_reversed(self):
        self.assertEqual(self.calc.add(35, 20), 55)

    def test_add_positive_negative(self):
        self.assertEqual(self.calc.add(-20, 10), -10)

    def test_add_negative_positive(self):
        self.assertEqual(self.calc.add(10, -20), -10)

    def test_add_two_negatives(self):
        self.assertEqual(self.calc.add(-50, -151), -201)

    def test_add_two_zeros(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_zero_non_zero(self):
        self.assertEqual(self.calc.add(0, 156), 156)


class TestCalcSubtract(TestCalcCase):
    
    def test_subtract_from_larger(self):
        self.assertEqual(self.calc.subtract(50, 26), 24)

    def test_subtract_from_lower(self):
        self.assertEqual(self.calc.subtract(20, 89), -69)

    def test_subtract_two_zeros(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_from_zero(self):
        self.assertEqual(self.calc.subtract(0, 20), -20)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(24, 0), 24)

    def test_subtract_negatives(self):
        self.assertEqual(self.calc.subtract(-60, -70), 10)


class TestCalcMultiply(TestCalcCase):

    def test_multiply_two_positives(self):
        self.assertEqual(self.calc.multiply(8, 9), 72)

    def test_multiply_two_negatives(self):
        self.assertEqual(self.calc.multiply(-10, -7), 70)

    def test_multiply_different_signs(self):
        self.assertEqual(self.calc.multiply(-6, 5), -30)

    def test_multiply_different_signs_reversed(self):
        self.assertEqual(self.calc.multiply(5, -6), -30)

    def test_multiply_one_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_multiply_two_zeros(self):
        self.assertEqual(self.calc.multiply(0, 0), 0)

    
class TestCalcDivide(TestCalcCase):

    def test_divide_without_remainder(self):
        self.assertAlmostEqual(self.calc.divide(24, 2), 12)

    def test_divide_with_remainder(self):
        self.assertAlmostEqual(self.calc.divide(35, 3), 11.666666666)

    def test_divide_equal(self):
        self.assertAlmostEqual(self.calc.divide(289, 289), 1)
    
    def test_divide_zero(self):
        self.assertAlmostEqual(self.calc.divide(0, 25), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(25, 0)

    def test_two_negatives(self):
        self.assertAlmostEqual(self.calc.divide(-20, -5), 4)


class TestCalcRandomOperation(TestCalcCase):

    def test_operation_add(self):
        random.randint = MagicMock(return_value=1)
        self.assertEqual(self.calc.random_operation(5, 6), self.calc.add(5, 6))

        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.subtract(5, 6))
        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.multiply(5, 6))
        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.divide(5, 6))

    def test_operation_subtract(self):
        random.randint = MagicMock(return_value=2)
        self.assertEqual(self.calc.random_operation(5, 6), self.calc.subtract(5, 6))

        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.add(5, 6))
        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.multiply(5, 6))
        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.divide(5, 6))

    def test_operation_multiply(self):
        random.randint = MagicMock(return_value=3)
        self.assertEqual(self.calc.random_operation(5, 6), self.calc.multiply(5, 6))

        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.add(5, 6))
        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.subtract(5, 6))
        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.divide(5, 6))

    def test_operation_divide(self):
        random.randint = MagicMock(return_value=4)
        self.assertEqual(self.calc.random_operation(5, 6), self.calc.divide(5, 6))

        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.add(5, 6))
        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.subtract(5, 6))
        self.assertNotEqual(self.calc.random_operation(5, 6), self.calc.multiply(5, 6))


if __name__ == '__main__':
    unittest.main()
