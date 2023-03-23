'''
Program: WAP to print the following patterns using loop
*       AAA     AAAAA
**      AA       AAAA
***     A         AAA 
****               AA
                    A
Author: Bikramadittya Bagchi
Date: 14-02-2021
'''
# Pattern 1
def patter1():
    num = int(input("Enter a number: "))
    for row in range(1, num+1):
        for col in range(1, row+1):
            print('*', end='')
        print()
# Pattern 2
def patter2():
    num = int(input("Enter a number: "))
    for row in range(num+1, 1, -1):
        for col in range(1, row):
            print("A", end='')
        print()
# Pattern 3
def patter3():
    num = int(input("Enter a number: "))
    for i in range (num, 0, -1): 
        print((num-i) * ' ' + i * 'A') 

# Main script
if __name__=="__main__":
    patter1()
    patter2()
    patter3()