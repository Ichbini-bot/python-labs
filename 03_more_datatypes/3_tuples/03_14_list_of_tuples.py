'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''


data = str(input("pls enter str: "))

list = data.split()
print(list)

list_2 = []
for item in list:
    list_3 = []
    for char in item:
        list_3.append(char)
    tup = tuple(list_3)
    list_2.append(tup)

print(list_2)





    





