#!/usr/bin/python3
""" Write a program that output whether a stor is open or closed, based on a giving day and hour of the week """


print("Enter your prepered day and hour: ")
day = int(input())
hour = int(input())

if day == 1 or day <= 5:
    if hour > 9 and hour <= 21:
        print("We're open!")
    else:
        print("Sorry we're closed for today, pls check back tomorrow.")
else:
    print("Sorry the store is closed today!")
