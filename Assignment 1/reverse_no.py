'''
Program: If two digit number is input through the keyboard. Write a program to reverse the number.
Author: Bikramadittya Bagchi
Date: 19-01-2021
'''
# Taking user input
num = int(input("Enter any number to reverse: "))

# Processing data
orig_no = num
s = 0
while num > 0:
    r = num % 10
    s = s*10 + r
    num = num // 10

# Display output
print(f"Original number is {orig_no}\nReversed number is {s}")