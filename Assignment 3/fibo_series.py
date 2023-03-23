"""
Program: Write a program to print first n fibonacci numbers
Author: Bikramadittya Bagchi
Date: 14-02-2021
"""
def printFibonacciNumbers():
    num = int(input("Enter n to print fibo nums: "))
    f1 = 0
    f2 = 1
    if (num < 1):
        return
    print(f1, end=" ")
    for x in range(1, num):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next

if __name__ == "__main__":
    printFibonacciNumbers()