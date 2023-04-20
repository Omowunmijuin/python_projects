#!/usr/bin/python3
'''program that uses list comprehensions to chech for consonants'''


print('Enter conconant numbers only: ')
word = input()

vowels = ['a','e','i','o','u','A','E','I','O','U']
consonant = [i for i in word if i not in vowels]
print(consonant)
