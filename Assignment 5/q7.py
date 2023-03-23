'''
Take input from the console and append it in a list and print the list.
'''

list1 = []
l = int(input("How many elements to insert in list: "))
for i in range(l):
    inp = input("Enter element to append: ")
    list1.append(inp)

print("List is: ", str(list1))