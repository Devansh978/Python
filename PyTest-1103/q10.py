'''
Print all three digits Armstrong number
Author: Bikramadittya Bagchi
Date: 11-03-2021
'''

def printArmstrong():
    print("Printing armstrong number in the range of 100-999")
    for i in range(100, 1000):
        sum = 0
        temp = i
        f_no = i
        c = 0
        while f_no > 0:
            r = f_no % 10
            f_no = f_no // 10
            c+=1
        while temp > 0:
            digit = temp % 10
            sum += digit ** c
            temp //= 10

        if i == sum:
            print(i,"is an Armstrong number")

def main():
    printArmstrong()

if __name__ == "__main__":
    main()