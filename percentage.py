#!/usr/bin/python3
'''Program that uses the LAMBDA function to check for percentage'''


print('Enter the price followed by the percentage: ')
price = int(input())
percentage = int(input())

check_perc = (lambda x, y: x * percentage / 100) (price, percentage)
print(check_perc)
