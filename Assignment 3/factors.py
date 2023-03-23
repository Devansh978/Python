'''
Program: WAP to display factors of an inputted number
Author: Bikramadittya Bagchi
Date: 08-02-2021
'''

num = int(input("Enter a number to find its factors: "))
print(f"Factors of {num} are: ")
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=' ')