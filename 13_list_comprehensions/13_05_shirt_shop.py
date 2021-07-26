'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

Desired output:
[["neon orange", "S"], ["neon orange", "M"], ["neon orange", "L"], ["spring green", "S"], ["spring green", "M"], ["spring green", "L"]]

'''
import itertools
import pprint

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

p = list(itertools.product(colors, sizes))

print(p)

print("VIA LIST COMPREHENSION")

def list_comprehension(list1, list2):
    carthesian = [[i,j] for i in list1 for j in list2]
    return carthesian

print(list_comprehension(colors, sizes))

print("VIA NESTED LOOP")

def nested_loop(list1, list2):
    carth = []
    for i in colors:
        for j in sizes:
            carth2 = []
            carth2.append(i)
            carth2.append(j)
            carth.append(carth2)
    return carth

print(nested_loop(colors, sizes))





