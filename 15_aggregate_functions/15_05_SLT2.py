courses = ["apple", "banana", "orange"]

list = []

for i in enumerate(courses):
    list.append(i)

print(list)

def alphabet():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        yield a

lorem = alphabet()

for i in lorem:
    print(i)

print("RETURN")

def alphabet():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        return a

print(alphabet())

seasons = ["Spring", "Summer", "Fall", "Winter"]

def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
        
seas = my_enumerate(seasons)

for i in seas:
    print(i)