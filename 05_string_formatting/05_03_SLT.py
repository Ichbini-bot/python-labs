
my_list = ["banana", "apple", 10]

print(my_list[1][2])

for item in my_list:
    print(f"Item in list: {item}")

def iterate_list(list):
    s = []
    for item in range(len(list)):
        s.append(list[item])
    return s

print("via function: ", iterate_list(my_list))


for item in range(len(my_list)):
    print(my_list[item])

'''
x = "Hello"
y = "World"

print(f"{x} {y:>50}")
'''