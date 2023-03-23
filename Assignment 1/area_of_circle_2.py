'''
Program: Write a program to calculate area of a circle and input for radius through keyboard.
Author: Bikramadittya Bagchi
Date: 18-01-2021
'''

import math

# Taking data from user using keyboard
radius = float(input("Please enter the radius of the circle: "))

# Processing data
area = math.pi * (radius ** 2)

# Display calculated area
print(f"Area of circle for radius {radius} is {area}")