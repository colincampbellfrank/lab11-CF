#https://github.com/colincampbellfrank/lab11-CF
# Partner 1: Colin Frank
#Could not get into contact with other partner

import math

def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    try:
        return (b / a)
    except ZeroDivisionError:
        return "ZeroDivisionError"

def logarithm(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        raise ValueError

def exp(a, b):
    return (a**b)

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

