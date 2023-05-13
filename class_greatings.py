#!/usr/bin/python3
"""Using class to create an object Greatings"""


class Greating:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def sayHi(self):
        if self.time == 0 or self.time < 12:
            print(self.name + " Says Good morning")
        elif self.time > 11 and self.time < 17:
            print(self.name + " Says Good afternoon")
        elif self.time > 16 and self.time < 21:
            print(self.name + " Says Good evening")
        elif self.time > 20 and self.time < 24:
            print(self.name + " Says Good night")
        else:
            print("Incorrect time selected")

print("Enter Your Name and the currentTime of the day to create a greating: ")
name = input()
time = input()
info = Greating(name, int(time))
info.sayHi()
