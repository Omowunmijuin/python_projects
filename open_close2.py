#!/usr/bin/python3
""" using the boolean logic to check if a store is open or not on a specific day and hour """


print("Enter your prefered day and hour: ")
day = int(input())
hour = int(input())

if (day == 1 or day <= 5) and (hour > 9 and hour <= 21):
    print("We're open!")
else:
    print("Sorry we're closed, check back tomorrow.")
