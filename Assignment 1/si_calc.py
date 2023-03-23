'''
Program: Write a program to calculate simple interest for a given principal, rate of interest,
and time. [Formula: I=P*t*i]
Author: Bikramadittya Bagchi
Date: 18-01-2021
'''

# Taking input from user
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the tenure in years: "))
rate = float(input("Enter the rate of interest % per annum: "))

# Processing data
si = principal*time*(rate/100)

# Display output
print(f'''\nEntered principal = {principal}\n
Entered Rate of Interest = {rate}% p.a.\n
Entered Tenure = {time}\n
Calculated Interest = {si}''')