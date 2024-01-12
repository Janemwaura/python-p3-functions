#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()


def greet(name):
    print(f"Hello, {name}!")
    return name

greet("Joy")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    
greet_with_default("Mark")    
greet_with_default()

def add(num1, num2):
    return num1 + num2

result = add(4,9)
print(result)

def halve(number):
    return number / 2

result = halve(40)
print(result)



