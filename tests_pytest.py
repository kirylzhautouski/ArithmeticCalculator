import pytest
import random

from math import isclose

from calculator import Calc


@pytest.fixture
def calc():
    return Calc()


def test_add_two_positives(calc):
    assert calc.add(20, 35) == 55


def test_add_two_positives_reversed(calc):
    assert calc.add(35, 20) == 55


def test_add_positive_negative(calc):
    assert calc.add(-20, 10) == -10


def test_add_negative_positive(calc):
    assert calc.add(10, -20) == -10


def test_add_two_negatives(calc):
    assert calc.add(-50, -151) == -201


def test_add_two_zeros(calc):
    assert calc.add(0, 0) == 0


def test_add_zero_non_zero(calc):
    assert calc.add(0, 156) == 156


def test_subtract_from_larger(calc):
    assert calc.subtract(50, 26) == 24


def test_subtract_from_lower(calc):
    assert calc.subtract(20, 89) == -69


def test_subtract_two_zeros(calc):
    assert calc.subtract(0, 0) == 0


def test_subtract_from_zero(calc):
    assert calc.subtract(0, 20) == -20


def test_subtract_zero(calc):
    assert calc.subtract(24, 0) == 24


def test_subtract_negatives(calc):
    assert calc.subtract(-60, -70) == 10


def test_multiply_two_positives(calc):
    assert calc.multiply(8, 9) == 72


def test_multiply_two_negatives(calc):
    assert calc.multiply(-10, -7) == 70


def test_multiply_different_signs(calc):
    assert calc.multiply(-6, 5) == -30


def test_multiply_different_signs_reversed(calc):
    assert calc.multiply(5, -6) == -30


def test_multiply_one_zero(calc):
    assert calc.multiply(0, 5) == 0


def test_multiply_two_zeros(calc):
    assert calc.multiply(0, 0) == 0


def test_divide_without_remainder(calc):
    assert calc.divide(24, 2) == 12


def test_divide_with_remainder(calc):
    assert isclose(calc.divide(35, 3), 11.666666666)


def test_divide_equal(calc):
    assert calc.divide(289, 289) == 1


def test_divide_zero(calc):
    assert calc.divide(0, 25) == 0


def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(25, 0)


def test_two_negatives(calc):
    assert calc.divide(-20, -5) == 4

 
def mock_randint(i):
    random.randint = lambda a, b: i 


def test_operation_add(calc):
    mock_randint(1)
    assert calc.random_operation(5, 6) == calc.add(5, 6)

    assert calc.random_operation(5, 6) != calc.subtract(5, 6)
    assert calc.random_operation(5, 6) != calc.multiply(5, 6)
    assert calc.random_operation(5, 6) != calc.divide(5, 6)


def test_operation_subtract(calc):
    mock_randint(2)
    assert calc.random_operation(5, 6) == calc.subtract(5, 6)

    assert calc.random_operation(5, 6) != calc.add(5, 6)
    assert calc.random_operation(5, 6) != calc.multiply(5, 6)
    assert calc.random_operation(5, 6) != calc.divide(5, 6)


def test_operation_multiply(calc):
    mock_randint(3)
    assert calc.random_operation(5, 6) == calc.multiply(5, 6)

    assert calc.random_operation(5, 6) != calc.add(5, 6)
    assert calc.random_operation(5, 6) != calc.subtract(5, 6)
    assert calc.random_operation(5, 6) != calc.divide(5, 6)


def test_operation_divide(calc):
    mock_randint(4)
    assert calc.random_operation(5, 6) == calc.divide(5, 6)

    assert calc.random_operation(5, 6) != calc.add(5, 6)
    assert calc.random_operation(5, 6) != calc.subtract(5, 6)
    assert calc.random_operation(5, 6) != calc.multiply(5, 6)