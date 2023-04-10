#!/usr/bin/python3
""" Write a program that checks and validates club entrance """


print("Enter your age to check if you are eligible for clubing: ")
age = int(input())

if age >= 18:
    print("Yay! let's go clubing.")
else:
    print("sorry champ! give it another try when you hit 18.")
