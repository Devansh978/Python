'''
Take the input from the console and create a 2D list.
'''

row = int(input("Enter how many rows: "))
col = int(input("Enter how many columns: "))

arr1 = [[0 for i in range(col)] for j in range(row)]
print("Insert elements for array: ")
for i in range(row):
    for j in range(col):
        print(f"Position {i+1}, {j+1}: ", end=' ')
        inp = int(input("Enter value: "))
        arr1[i][j] = inp

print(arr1)