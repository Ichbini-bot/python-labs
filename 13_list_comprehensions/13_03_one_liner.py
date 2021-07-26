'''
Use a one-line list comprehension to express the following functionality:

letters = []

for letter in 'suchalongword':
    letters.append(letter)

print(letters)

'''
letters = []

for letter in 'suchalongword':
    letters.append(letter)

print(letters)

print("VIA LIST COMPREHENSION")

def long_word():
    let = [letter for letter in "suchalongword"]
    return let

print(long_word())