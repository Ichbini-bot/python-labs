'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

list = ["apple", "pears", "kiwis", "pineapples"]
list2 = [1,2,3,4,5]

def my_enumerate(argument, start = 0):
      index = start
      for element in argument:
            yield index, element #first time using yield. Compared to return, yiel can give back several values - however, needs to be called via a for loop (as iterator)
            index +=1

for i in my_enumerate(list):
      print(i)

for i in my_enumerate(list2):
      print(i)


