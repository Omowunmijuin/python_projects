#!/usr/bin/python3
"""Using the Player class, with its attributes and an intro() method to make a vedio game"""

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")
