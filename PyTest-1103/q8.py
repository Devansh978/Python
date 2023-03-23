'''
Print the following:
    a
    b c
    d e f
    g h i j
Author: Bikramadittya Bagchi
Date: 11-03-2021
'''

def printPat():
    num  = int(input("Enter a number: "))
    c = 1
    for row in range(1, num+1):
        for col in range(1, row+1):
            print(chr(c+96), end=" ")
            c += 1
        print()

def main():
    printPat()

if __name__ == "__main__":
    main()