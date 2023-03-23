'''
Build a dictionary with two keys, 'a' and 'b', each having an associated value of 0(using two method)
'''
# Method 1
keys = ['a', 'b']
values = [0, 0]

print("Keys are: ", str(keys))
print("Values are: ", str(values))

D1 = {keys[i]:values[i] for i in range(len(keys))}
print("Dictionary is: ", str(D1))

# Method 2
keys = ['a', 'b']
values = [0, 0]

print("Keys are: ", str(keys))
print("Values are: ", str(values))

D2 = {}
for key in keys:
        for value in values:
                D2[key] = value
                values.remove(value)
                break
print("Dictionary is: ", str(D2))