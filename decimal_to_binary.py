#!/usr/bin/python3
""" Program that uses Recursion to convert an input function from Decimal to Binary """


def convert(num):
    if num == 1:
        return True
    return (num % 2 + 10 * convert(num // 2))

fix = int(input())
print(convert(fix))
