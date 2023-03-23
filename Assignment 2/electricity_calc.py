'''
Program: WAP to input consumed unit and calculate Electricity Bill, where monthly rent Rs. 300.
Unit        Charge per unit(Rs.)
Upto 300        7
301- 800        9
801-1500        12
1501 & above    15
Author: Bikramadittya Bagchi
Date: 02-02-2021
'''
# Declarations
total = 0.0
print("***Electricity bill calculator***")

# Taking input from users
while True:
    try:
        inp = input("Please enter the units consumed: ")
        inp = int(inp)
        break
    except ValueError:
        print("Not a valid input! Enter units in numbers only!")
if inp >= 0:
    min_rent = 300
    # Processing data
    if inp <= 300:
        if (inp * 7) < min_rent:
            total = min_rent
        else:
            total = inp * 7
    elif 300 < inp <= 800:
        total = ((inp - 300) * 9) + (300 * 7)
    elif 800 < inp <= 1500:
        total = (300 * 7) + (500 * 9) + ((inp - 800) * 12)
    else:
        total = (300 * 7) + (500 * 9) + (700 * 12) + ((inp - 1500) * 15)
    # Display output
    print(f"Consumed unit: {inp}")
    print(f"Your total bill {total}")
else:
    print("Invalid unit entered!")