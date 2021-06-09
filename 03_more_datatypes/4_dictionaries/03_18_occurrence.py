'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

data = input("pls enter word or sentence: ")
l1 = list(data.replace(" ", ""))

dictionary = dict()

for x in l1:
    dictionary[x] = l1.count(x)

print(dictionary)


'''
data = input("pls enter a sentence: ")
# Remove spaces between words
data_stripped = data.replace(" ", "")
print(data_stripped)

# empty dictionnary
dictionnary = dict()

for char in data_stripped:
    dictionnary[char] = data_stripped.count(char)

print(dictionnary)
'''