'''
Program: WAP to display all prime numbers upto n
Author: Bikramadittya Bagchi
Date: 08-02-2021
'''

rng_prm = int(input("Enter the number: "))

print(f"Prime numbers upto {rng_prm} are: ")

for num in range(2, rng_prm + 1):
    if num > 1:
       for i in range(2, num):
           if num % i == 0:
               break
       else:
           print(num, end=" ")
