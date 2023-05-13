#!/usr/bin/python3
"""Using class to create an object Greatings"""


class Greating:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def sayHi(self):
        print(self.name + "Says Hi, " + self.time)

name = input()
time = input()
info = Greating(name, time)
info.sayHi()
