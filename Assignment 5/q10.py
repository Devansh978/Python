'''
Given a Python list of numbers. Turn every item of a list into its square
'''
size = int(input("Enter size of list: "))
l1 = []

for i in range(size):
    inp = int(input("Enter value for list: "))
    l1.append(inp)

print("Original list: ", l1)

for i in range(size):
    l1[i] = l1[i] ** 2

print("Item value squared list: ", l1)
