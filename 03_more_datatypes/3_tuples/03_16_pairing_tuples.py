'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

list = []

while True:
    data = input("enter numbers (type stop to quit): ")
    if data == "stop": break
    list.append(data)
list.sort() 
print("you entered the following numbers: ", list)

x = len(list)
if x %2 == 1:
    list.append(0)
    print("as we need an even list for this program, the value 0 hast been appended: ", list)


counter1 = 0
counter2 = 2

for i in range (0, len(list)):
    new_list = []
    for i in range(counter1, counter2): 
            new_list.append(list[i])
    tupe = tuple(new_list)
    print(tupe)
    counter1 += 2
    counter2 += 2
    if counter2 > len(list):
        break
    '''
    not needed
    else:
        continue
    '''



    




