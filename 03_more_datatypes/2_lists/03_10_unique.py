'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_list = []


for x in list:
    if list.count(x) < 2:
        unique_list.append(x)
print(unique_list)
'''
for x in list:
    if list.count(x) > 1:
        while x in list:
            list.remove(x)
print(list)
'''