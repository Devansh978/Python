"""
Program: Write a program to check the given number is prime or not
Author: Bikramadittya Bagchi
Date: 08-02-2021
"""

num = int(input("Enter any number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
