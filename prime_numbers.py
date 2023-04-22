#!/usr/bin/python3
"""Program that uses Generator to output prime numbers"""


def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for i in range (2, x):
        if x % i == 0:
            return False
    return True

def primeGenerator(a, b):
    while a < b:
        if isPrime(a):
            yield a
        a += 1


print('Enter random numbers to output prime numbers from: ')
firstNumber = int(input())
lastNumber = int(input())

print(list(primeGenerator(firstNumber, lastNumber)))
