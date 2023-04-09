#!/usr/bin/python3
""" Writa a program that reapeat an input at the giving number of time using a for loop """


print("Enter something to be repeated: ")
random_input = str(input())
print("Enter number of time to be printed: ")
random_num = int(input())

names = ""
for random in range(random_num):
    names += random_input + " "
    random += 1
print(names)
