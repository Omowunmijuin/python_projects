#!/usr/bin/python3
""" An ATM program that calculate and display a balance remaining after a withdrawal."""

print("Enter your initial balance, followed by your withdrawal amount: ")
initialBalance = int(input())

print("Amount to withdraw: ")
withdrawal = int(input())

initialBalance -= withdrawal
print("Your remaining balance is: " + str(initialBalance)) 
