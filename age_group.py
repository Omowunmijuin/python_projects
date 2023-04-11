#!/usr/bin/python3
""" Using the Boolean logic to document and handle user age groups """


age = int(input())

if age > 0 and age <= 11:
    print("Child")
elif age >= 12 and age < 18:
    print("Teen")
elif age == 18 or age < 65:
    print("Adult")
else:
    print("Age group not found!")
