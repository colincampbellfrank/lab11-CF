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
    if a==0:
        raise ZeroDivisionError
    else:
        return(b / a)   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a<=0 or b<0:
        raise ValueError
    else:
        math.loga(b)

def exponent(a, b):
    return (a^b)

print(divide(0,1))


