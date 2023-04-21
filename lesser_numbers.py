#!/usr/bin/python3
"""program that uses the filter() function to check for lesser numbers"""


nums = [19, 28, 17, 70, 7, 39, 9]

small_numbers = list(filter(lambda x: x < 20, nums))
print(small_numbers)
