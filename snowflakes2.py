#!/usr/bin/python3
""" draw a snow flake using for loop and if conditioning """


i = 0
for i in range(5):
    if i == 0 or i == 4:
        print("  *  ")
    elif i == 1 or i == 3:
        print(" *** ")
    else:
        print("*****")
