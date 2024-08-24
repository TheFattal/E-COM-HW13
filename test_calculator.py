# from Terminal > pip install pytest
# from Terminal > pytest .

import pytest
import calculator


def test_calculator_add_small():
    # Arrange
    x: int = -1
    y: int = 0
    expected: int = -1

    # Act
    actual: int = calculator.add(x, y)

    # Assert
    assert actual == expected


def test_calculator_sub_small():
    # Arrange
    x: int = 14
    y: int = 7
    expected: int = 7

    # Act
    actual: int = calculator.subtract(x, y)

    # Assert
    assert actual == expected


def test_calculator_mul_small():
    # Arrange
    x: int = 8
    y: int = 9
    expected: int = 72

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected


def test_calculator_mul_zero():
    # Arrange
    x: int = 1000
    y: int = 0
    expected: int = 0

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected


def test_calculator_div_small():
    # Arrange
    x: int = 99
    y: int = 11
    expected: int = 9

    # Act
    actual: int = calculator.divide(x, y)

    # Assert
    assert actual == expected


def test_calculator_div_zero_error_phase1():
    # test that we get an error when divide by zero
    # Arrange
    x: int = 99
    y: int = 0

    # Act
    try:
        actual: int = calculator.divide(x, y)
        assert False  # fail the test
    except ZeroDivisionError as e:
        assert True  # pass the test


def test_calculator_div_zero_error_phase2():
    x: int = 99
    y: int = 0
    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = calculator.divide(x, y)

    assert str(ex.value) == "Cannot divide by zero!"


# d:
def test_power_2_4():
    # Arrange
    base = 2
    exponent = 4
    expected = 16

    # Act
    actual = calculator.power(base, exponent)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# e:
def test_power_3_2():
    # Arrange
    base = 3
    exponent = 2
    expected = 9

    # Act
    actual = calculator.power(base, exponent)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# f:
def test_power_9_0():
    # Arrange
    base = 9
    exponent = 0
    expected = 1

    # Act
    actual = calculator.power(base, exponent)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# g:
def test_sqrt_25():
    # Arrange
    number = 25
    expected = 5

    # Act
    actual = calculator.sqrt(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# h:
def test_sqrt_negative():
    # Arrange
    number = -5

    # Act & Assert
    with pytest.raises(ValueError, match="math domain error"):
        calculator.sqrt(number)


# i:
def test_prime_is_1():
    # Arrange
    number = 1
    expected = False

    # Act
    actual = calculator.is_prime(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# j:
def test_prime_is_2():
    # Arrange
    number = 2
    expected = True

    # Act
    actual = calculator.is_prime(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# k:
def test_prime_is_16():
    # Arrange
    number = 16
    expected = False

    # Act
    actual = calculator.is_prime(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# l:
def test_prime_is_negative():
    # Arrange
    number = -3
    expected = False

    # Act
    actual = calculator.is_prime(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# m:
def test_prime_is_0():
    # Arrange
    number = 0
    expected = False

    # Act
    actual = calculator.is_prime(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# n:
def test_factorial_4():
    # Arrange
    number = 4
    expected = 24

    # Act
    actual = calculator.factorial(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# o:
def test_factorial_0():
    # Arrange
    number = 0
    expected = 1

    # Act
    actual = calculator.factorial(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# p:
def test_factorial_1():
    # Arrange
    number = 1
    expected = 1

    # Act
    actual = calculator.factorial(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# q:
def test_factorial_5():
    # Arrange
    number = 5
    expected = 120

    # Act
    actual = calculator.factorial(number)

    # Assert
    assert actual == expected, f"Expected {expected}, but got {actual}"


# r:
def test_factorial_negative():
    # Arrange
    number = -3

    # Act & Assert
    with pytest.raises(ValueError, match="Factorial not defined for negative values"):
        calculator.factorial(number)
