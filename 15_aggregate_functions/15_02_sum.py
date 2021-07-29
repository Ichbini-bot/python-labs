'''
Write a simple aggregate function, sum(), that takes a list and returns the sum.

'''

list = [1,2,3,4]
print("The sum of the list is: ", sum(list))

#Crowbar method:

def summe(argument):
    total = 0
    for i in argument:
        total = total + i
    return total
print("The sum of the list is (crowbar method): ", summe(list))


