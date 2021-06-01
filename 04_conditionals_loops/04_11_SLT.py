'''
people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]


# Change everything below here to use while loops instead
for person in people:
    to_print = ""
    for name in person:
        to_print += name + " "
    print(to_print)

''' 
'''
people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

i = 0
while i < len(people):
    sub_list = people[i]
    j = 0
    while j < len(sub_list):
        to_print = sub_list[j]
        j += 1
        print(to_print)
          
    i += 1  
'''
people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]
i = 0
while i < len(people):
    person = people[i]
    to_print = ""
    j = 0
    while j < len(person):
        name = person[j]
        to_print += name + " "
        j += 1
    print(to_print)    
    i += 1
        
'''
counter = 0
sum = 0
while (counter < 10):
    sum += counter
    counter += 3
print(counter)
print(sum)
'''
'''
name = ''                              # (1)

while name != 'your name':             # (2)
    print('Please type your name.')
    name = input()                     # (3)

print('Thank you!')                    # (4)
'''



'''
total = 0

example_list = [2, 5, 7, 9, 3, 8, 8]

for num in range (0, len(example_list)):
    total = total + example_list[num]
    
print(total)

total = 0

example_list = [2, 5, 7, 9, 3, 8, 8]

for num in example_list:
    total = total + example_list[num]
    
print(total)
'''

'''
for i in range(1, 11):
    print(i)
'''
'''
my_list = [1, 2, 3, 4, 5]

# 'break' ends the execution of the loop, skipping anything after
for num in my_list:
  if num % 3 == 0:
    break
  print(num)
print("finished 'break' part")

# 'continue' returns to the beginning of the loop, skipping anything after in that specific run
# it starts the loop again with the next item
for num in my_list:
  if num % 3 == 0:
    continue
  print(num)
print("finished 'continue' part")
'''
'''
fruit = input("enter fruit: ")
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


fruit = input("enter fruit: ")
index = len(fruit) -1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1
'''
'''
users = {'mary': 22, 'caroline': 26, 'harry': 20, "tobi": 40}
# let's make them age for 30 years each!

for user, age in users.items():
    aged = age + 30
    print(user, aged)
'''

'''
my_list = [1, 2, 3, "hello", "it's blue!", 10]

for item in my_list:
    print(item)
'''

'''
x = 5

y = 10
if x < 5:
    print("one")
elif x > 5:
    print("two")
else:
    print("three")
if x >= 5 and y < 10:
    print("four")
elif x < y and  y == 10:
    print("five")
else:
    print("six")
'''
'''
flag = True
if not flag:
    print("Option A")
else:
    print("Option B")
'''

'''
while True:
    data = input("please enter a sentence (type quit to abort): ")
    data_len = len(data)
    print(data, "length is: ", data_len)

    if data == "quit":
        break
    
print("Done")

for i in range(1, 5):

    data = input("please enter a sentence (type quit to abort): ")
    data_len = len(data)
    print(data, "length is: ", data_len)

    if data == "quit":
        break
    
print("Done")
'''
