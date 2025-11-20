"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    try:
        return (b / a)
    except ZeroDivisionError:
        return "ZeroDivisionError"

def logarithm(a, b):
    try:
        return math.loga(b)
    except ValueError:
        return "ValueError"

def exponent(a, b):
    return (a^b)

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return "ValueError"

def hypotenuse(a, b):
    return math.hypot(a, b)



