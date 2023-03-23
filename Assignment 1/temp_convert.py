'''
Program: Write a program to convert temparature Farhenheit to Celsius
Author: Bikramadittya Bagchi
Date: 19-01-2021
'''
# Taking user input
far_inp = float(input("Enter the temparature in Farhenheit: "))
# Processing data
cel_out = (5/9)*(far_inp-32)
# Show data
print(f"Temparature {far_inp} Farhenheit is {cel_out} Celsius")