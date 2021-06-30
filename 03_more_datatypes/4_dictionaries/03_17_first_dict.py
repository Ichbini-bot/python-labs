'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

dictionary = dict()

for entry in range(1, 11):
    dictionary[entry] = entry**2

print(dictionary)

'''
# Not so elegant solution
keys = []
key = 0


for key in range(0, 10):
    key += 1
    keys.append(key)

values = []

for value in keys:
    value = value**2
    values.append(value)

print(values)

dictionnary = dict(zip(keys, values))
print(dictionnary)
print("---------------")

# elegant solution:
n = int(input("pls enter number: "))
dictionnary_direct = dict()

for x in range(1, n+1):
    dictionnary_direct[x] = x*x

print(dictionnary_direct)
'''