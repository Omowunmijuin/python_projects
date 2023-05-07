#!/usr/bin/python3
""" Program that returns the smallest argument """


def my_min(*args):
    return min(*args)

print(my_min(7, 19, 10, 4, 147, 74))
