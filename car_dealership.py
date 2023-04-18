#!/usr/bin/python3
"""Program that uses dictionary to check for car data"""


carData = {'brand': 'Toyota',
        'year': '2020',
        'color': 'black'
        }

print('Enter car data: ')
carType = input()

print(carData)
print(carData[carType])
