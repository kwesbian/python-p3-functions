#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
            # The code above checks if the variable `number` is not  an instance of the `int` or `float` data type.
            # `isinstance` => checks if a variable is a certain data type.
            # `(int, float)` => tuple being checked. isinstance checks whether `number` is an instance of either the int class or the float class.
        return None
    
    return number / 2