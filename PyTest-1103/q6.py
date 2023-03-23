'''
Print the following.
    0
    1 0
    0 1 0
    1 0 1 0
Author: Bikramadittya Bagchi
Date: 11-03-2021
'''

def patt_print():
    n = int(input("Please give range to print pattern: "))
    for row in range(1, n+1):
        for col in range(1, row+1):
            if (row+col)%2 == 0:
                print(0, end=" ")
            elif (row+col)%2 != 0:
                print(1, end=" ")
            else:
                print(" ")
        print()

def main():
    patt_print()

if __name__ == "__main__":
    main()
    