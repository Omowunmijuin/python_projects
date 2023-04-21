#!/usr/bin/python3
"""program that uses the map() function to increase salaries"""


print('Enter bonus: ')
salaries = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
bonus = int(input())

def bonus_salary(x):
    return x + bonus

salary_increase = list(map(bonus_salary, salaries))
print(salary_increase)
