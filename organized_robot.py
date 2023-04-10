#!/usr/bin/python3
""" Program will be use in a robot to categorize items by their colors """


print("Choose a color: ")
color = input()

print("Available colors are: [Red, Green, Blue, Yellow, Black]")
items = red, green, blue, yellow, black 
items = color

if color is red:
    print("box #1")
elif color is green:
    print("box #2")
elif color is blue:
    print("box #3")
elif color is yellow:
    print("box #4")
elif color is black:
    print("box #5")
else:
    print("Unknown color")
