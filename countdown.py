#!/usr/bin/python3
""" Write a program that countdown from a giving input """


print("Enter a second to count down from: ")
seconds = int(input())

while seconds >= 0:
    print(seconds)
    seconds -= 1
