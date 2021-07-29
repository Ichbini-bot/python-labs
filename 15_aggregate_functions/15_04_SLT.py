courses = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

for word in range(len(courses)):
    print(f"{word}: {courses[word]} python")

for i, c in enumerate(courses):
    print(f"{i}: {c} python")

for i in enumerate(courses):
    print(i)
# enumerate returns two loop variables (in form of a tuple), consisting of the iterator and the string (0, "Intro"), (1, "Intermediate")
# BTW: ARGUMENT UNPACKING (*ARGS, **KWARGS) 

for i, c in enumerate(courses, start = 1): #very POWERFUL! (Count starts at 1, however the iterator for the value at 0!)
    print(i, c)

alphabet = "abcdefghijklmnopqrstuvwxyz"

def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

def even_items2(it):
    return [v for v in it if not v % 2]

print(even_items(alphabet))
print(even_items(alphabet))

def alphabet():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        yield a

lorem = alphabet()

print(alphabet())


seasons = ["Spring", "Summer", "Fall", "Winter"]

def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
        

print(my_enumerate(seasons))

my_list = ["apple", "banana", "orange"]

obj1 = enumerate(my_list)

print(obj1)
