'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

Modulo

'''
'''
gen = (x for x in range(1, 10000))

for number in gen:
    if number % 1111 == 0:
        print(number)
'''

gen = (x for x in range(1,10000) if x % 1111 == 0)

for num in gen:
    print(num)