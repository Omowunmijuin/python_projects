#!/usr/bin/python3
"Program that uses the get() function to get a value"""


data = { 77: 'Australia',
    49: 'United states',
    23: 'Germany',
    27: 'Canada',
    27: 'Nigeria',
    43: 'China',
    17: 'United Kingdom',
    47: 'Italy'
    }
print('Enter a number to choose your prefered country: ')
print(data)
country = int(input())
print(data.get(country, "Not found"))
