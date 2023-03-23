'''
Write a program to convert temperature Celsiusto Fahrenheit and vice versa.
Author: Bikramadittya Bagchi
Date: 11-03-2021
'''

def fToC(far_inp):
	cel_out = (5/9)*(far_inp-32)
	print(f"Temparature {far_inp} Farhenheit is {cel_out} Celsius")

def cToF(cel_inp):
	far_out = (cel_inp * 9/5) + 32
	print(f"Temparature {cel_inp} Celsius is {far_out} Farhenheit")

def main():
	inp1 = float(input("Enter farhenheit temparature for converting into celsius: "))
	fToC(inp1)
	inp2 = float(input("Enter celsius temparature for converting into farhenheit: "))
	cToF(inp2)

if __name__=="__main__":
	main()