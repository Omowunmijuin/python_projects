#!/usr/bin/python3
""" Program will be use in a robot to categorize items by their colors """


print("Choose a color: ")
color = input()

print("Available colors are: [Red, Green, Blue, Yellow, Black]")
item = ['red', 'green', 'blue', 'yellow', 'black']
item = color

if item == 'red':
    print("box #1")
elif item == 'green':
    print("box #2")
elif item == 'blue':
    print("box #3")
elif item == 'yellow':
    print("box #4")
elif item == 'black':
    print("box #5")
else:
    print("Unknown color")
