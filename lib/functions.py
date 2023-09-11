#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")

def greet(name):
    pass
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Sunny")

def add(num1, num2):
    return num1 + num2
add(1, 2)

def halve(number):
    if not (isinstance(number, (int, float))):
        return None
    return (number) / 2

# print(halve(4.8))
# print(type('hello'))