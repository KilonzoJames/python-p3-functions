#!/usr/bin/env python3
'''
This is a sample module docstring.
'''
def greet_programmer():
    '''
    This function greet a programmer.
    '''
    print("Hello, programmer!")
print(greet_programmer())

def greet(name):
    '''
    This function greet a person.
    '''
    print(f"Hello, {name}!")
print(greet("Naureen"))

def greet_with_default(name="programmer"):
    '''
    This function greet a person with a default name.
    '''
    print(f"Hello, {name}!")
print(greet_with_default("Sunny"))

def add(num1, num2):
    '''
    This function adds two numbers.
    '''
    return num1 + num2
print(add(45,55))

def halve(number):
    '''
    This function halves a number.
    '''
    if not isinstance(number, (int, float)):
        return None
    else:
        return number/2
print(halve(7))
