l1 = [20, 11, 2, 10, 5, 16, 20]
fruit = ["apple", "kiwi", "melon", "banana", "pear", "mango", "apple"]

list1 = ("apple", "kiwi")
list2 = ("banana", "apple", "luck", "banana", "apple", "luck")

users = [{"fullname": "Isaac Asimov", "book" : "robot dreams"}, {"fullname": "Alastair Reynolds", "book" : "chasm City"}, {"fullname": "H.G Wells", "book" : "time machine"}, {"fullname" : "George Orwell", "book" : 1984}]


users1 = {"mary": 22, "caroline": 26, "harry": 22}
users3 = {"cory": 60}

users1.update(users3)
print(users1)

users2 = {"fullname": "Isaac Asimov", "book" : "robot dreams"}

for names in users1.items():
    fl = list(names)
    print(fl)

for item in users:
    print(item["fullname"])
    first_last = item["fullname"].split()
    print(first_last)
    







