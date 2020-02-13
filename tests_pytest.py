import pytest
import random

from math import isclose

from calculator import Calc


@pytest.fixture
def calc():
    return Calc()


@pytest.mark.parametrize('a, b, expected_result', [
    (20, 35, 55), 
    (35, 20, 55),
    (-20, 10, -10),
    (10, -20, -10),
    (-50, -151, -201),
    (0, 0, 0),
    (0, 156, 156)    
])
def test_add(calc, a, b, expected_result):
    assert calc.add(a, b) == expected_result


@pytest.mark.parametrize('a, b, expected_result', [
    (50, 26, 24),
    (20, 89, -69),
    (0, 0, 0),
    (0, 20, -20),
    (24, 0, 24),
    (-60, -70, 10)
])
def test_subtract(calc, a, b, expected_result):
    assert calc.subtract(a, b) == expected_result


@pytest.mark.parametrize('a, b, expected_result', [
    (8, 9, 72),
    (-10, -7, 70),
    (-6, 5, -30),
    (5, -6, -30),
    (0, 5, 0),
    (0, 0, 0)
])
def test_multiply(calc, a, b, expected_result):
    assert calc.multiply(a, b) == expected_result


@pytest.mark.parametrize('a, b, expected_result', [
    (24, 2, 12),
    (35, 3, 11.666666666),
    (289, 289, 1),
    (0, 25, 0),
    (-20, -5, 4)
])
def test_divide(calc, a, b, expected_result):
    assert isclose(calc.divide(a, b), expected_result)


def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(25, 0)

 
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