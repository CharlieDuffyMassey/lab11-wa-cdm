import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
def square_root(a):
    # if a < 0:
    #     raise ValueError
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as b:
            print(b)

def hypotenuse(a, b):
    return math.hypot(a, b)

   # math.hypot(a,b)
# First example

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a <= 0 or a ==  1 or b <= 0:
        raise ValueError("Invalid value(s).")
    return math.log(b, a)
def exp(a, b):
    return a ** b