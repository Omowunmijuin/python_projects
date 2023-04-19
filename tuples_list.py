#!/usr/bin/python3
'''program that iterate through a tuples within a list'''


contacts = [
        ('Tobi', 27),
        ('Omowunmi', 24),
        ('Fathia', 11),
        ('Balikis', 30),
        ('Akeem', 57),
        ('William', 25),
        ('Kamil', 78)
]


print('Enter your name as keyword to get your age: ')
name = str(input())

for names in contacts:
    if name in names:
        print(str(names[0]) +' is ' + str(names[1]))
        break
    else:
        print('Not Found')
