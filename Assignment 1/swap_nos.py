'''
Program: Two numbers are input through the keyboard into two location C and D.
Write a program to interchange the contents of C and D
Author: Bikramadittya Bagchi
Date: 19-01-2021
'''
# Taking user input
num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

# swapping two numbers without using temporary variable
num1, num2 = num2, num1

print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)