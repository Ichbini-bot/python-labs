
'''
x = tuple([1, 2, "hello",])
print(x)
print(len(x))

singleton = "hello",
print(len(singleton[0]))
'''
'''
numbers = [42, 1, 10]
numbers += [5]
numbers.remove(numbers[1])
numbers.sort()
print(numbers)
'''

'''
numbers = [5, 2, 3]
numbers.insert(0, 10, 5)
print(numbers)
'''


'''
bucket_list = ["climb Mt. Everest", "eat fruits from a tree", "raise a child"]
print(bucket_list[0])
bucket_list[1] += " that I planted"
print(bucket_list)
print(bucket_list[1])

bucket_list += ["live in Barca", "work at Google"]
print(bucket_list)
bucket_list.remove(bucket_list[-1])
print(bucket_list)

for task in bucket_list:
    print(task)
'''
'''
longset = {1, 2, 3, 4, 5, 6, 42, 50, 9}
s1 = {1, 7, 8}

print(longset | s1)
print(longset.union(s1))

print(longset & s1)
print(longset.intersection(s1))
'''
'''
numbers = [42, 10, 42]
unique_nums = set(numbers)
print(unique_nums)

'''
'''
users = {'mary': 22, 'caroline': 26, 'harry': 22}
print(users["harry"])
users["harry"] = 20
print(users["harry"])
'''

my_dict = {1: "hi"}
print(my_dict[1])



my_dict = {}
my_dict[1] = "hi"
print(my_dict[1])