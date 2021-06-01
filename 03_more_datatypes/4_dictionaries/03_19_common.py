'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = {"a": 2, "c": 4 , "d": 2}

dic3 = dict()

for key1, value1 in dic1.items():
    if key1 not in dic2:
        dic3[key1] = value1
        print(dic3)

for key2, value2 in dic2.items():
    if key2 not in dic1:
        dic3[key2] = value2
        print(dic3)
for key1, value1 in dic1.items():
    for key2, value2 in dic2.items():
        if key1 in dic2:
            dic3[key1] = value1 + value2
    print(dic3)

print(dict(sorted(dic3.items())))
        
    


'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = dict()

for key in dict_1:
    if key in dict_2:
        new_value = dict_1[key] + dict_2[key]
        result.update(new_value)
    else:
        new_value = dict_1[key]

print(new_value)
'''