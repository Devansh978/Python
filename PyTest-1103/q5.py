'''
Print Fibonacci series < 100. Also print reverse Fibonacci series.
Author: Bikramadittya Bagchi
Date: 11-03-2021
'''

def printFibonacciNumbers():
    num = int(input("Enter range to print Fibonacci series: "))
    t1 = 0; t2 = 1; nextTerm = 0;
    lFibo = []
    lFibo.append(t1)
    lFibo.append(t2)
    nextTerm = t1+t2
    while nextTerm <= num:
        lFibo.append(nextTerm)
        t1 = t2
        t2 = nextTerm
        nextTerm = t1 + t2
    
    print(f"The fibonacci series upto {num} in sequential order: ")
    for i in lFibo:
        print(i, end=" ")
    print()

    print(f"The fibonacci series upto {num} in reverse order: ")
    for i in lFibo[::-1]:
        print(i, end=" ")

def main():
    printFibonacciNumbers()

if __name__ == "__main__":
    main()