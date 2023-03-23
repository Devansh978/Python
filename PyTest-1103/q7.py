'''
Print the prime numbers between 100 and 30.
Author: Bikramadittya Bagchi
Date: 11-03-2021
'''

def rangePrime(start, end):
    for num in range(start, end + 1, -1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=" ")

def main():
    st1 = int(input("Enter the starting point: "))
    en1 = int(input("Enter the ending point: "))
    rangePrime(st1, en1)

if __name__ == "__main__":
    main()