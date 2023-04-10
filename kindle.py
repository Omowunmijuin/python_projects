#!/usr/bin/python3
""" Write a program that take the user age and output Take your kindle! if age is under or equal to 19 """


print("Enter your age for a free kindle: ")
age = int(input())

if age <= 19:
    print("Take your kindle!")
else:
    print("Sorry no kindle for you!")
