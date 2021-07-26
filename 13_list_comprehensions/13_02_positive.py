'''
Using list comprehension, create a list "positive" from the list
"numbers" that contains only the positive numbers from the list "numbers".

'''

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]

positive = []

for num in numbers:
    if num > 0:
        positive.append(num)

print(positive)

print("VIA LIST COMPREHENSION")

def find_positive(list):
    pos = [i for i in list if i > 0]
    return pos

print(find_positive(numbers))

