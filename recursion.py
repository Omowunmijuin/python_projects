#!/usr/bin/python3
""" program that uses Recursion """


def fibonacci(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
print(fibonacci(7))
