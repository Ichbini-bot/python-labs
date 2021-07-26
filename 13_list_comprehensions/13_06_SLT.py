letters = [i for i in "codingnomads"]

print(letters)

letter = []

for char in 'CodingNomads':
    letter.append(char.lower())

print(letter)

class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("There was a problem")
except Exception as e:
    print(e)