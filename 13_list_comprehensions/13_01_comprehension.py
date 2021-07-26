'''
Using list comprehension, create a list that contains the individual
letters using the word "CodingNomads".

For example:

word = "CodingNomads"
..your code
result_list = ['C', 'o', 'd', 'i', 'n', 'g', 'N', 'o', 'm', 'a', 'd', 's']

'''
b = "coding"
word = "CodingNomads"
list = []
for char in word:
    list.append(char)

print(list)

print("VIA LIST COMPREHENSION")

def list_comp(variable):
    list = [i for i in variable]
    return list

print(list_comp(word))

