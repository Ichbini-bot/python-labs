fruits = ["Kiwi", "Apple", "Melon"]

tupe_result = []

for i in range(0, 3):
    tupe_result.append(tuple(fruits[i]))
print(tupe_result)

new_list = []

for i in range(0, 3):
    sublist = []
    sublist.append(fruits[i])
    new_list.append(tuple(sublist))

print(new_list)

list1 = "this is a string"

list2 = list1.replace(" ", "")
print(list2)
