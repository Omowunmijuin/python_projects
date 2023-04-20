#!/usr/bin/python3
'''Program that uses for loop and append() function to check for consonants'''


print('Enter only consonant letters only: ')
word = list(input())
vowels = ('a','e','i','o','u','A','E','I','O','U')
consonant = []

for i in word:
    if i not in vowels:
        consonant.append(i)
else:
    print('Vowels not allowed')

print(consonant)
