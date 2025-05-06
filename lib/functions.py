#!/usr/bin/env python3

def greet_programmer():
    print(f"Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

    # greet("Guido van Rossum")

def greet_with_default(name ="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2
add(1, 2)

def halve(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Please use numeric types (int or float) only")
    return number / 2
