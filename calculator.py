import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


# a:
def power(a, b):
    return a ** b


# b:
def sqrt(a):
    return math.sqrt(a)


# c:
def is_prime(a):
    if a <= 1:
        return False
    if a == 2:
        return True  # 2 is the only even prime number
    if a % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(a)) + 1, 2):  # The most efficient way
        if a % i == 0:
            return False
    return True


def factorial(a):
    if a < 0:
        raise ValueError("Factorial not defined for negative values")
    elif a == 0 or a == 1:
        return 1
    else:
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result


# testing:
# check all cases
# auto keep functionality working
# make QA life more simple
# keep bug fix working
