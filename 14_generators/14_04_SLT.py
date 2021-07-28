'''
list = [x for x in range(5)]

print(list)

print("---GEN---")

gen = (x for x in range(5))

print(gen)
for i in gen:
    print(i)
'''

gen = (x for x in range(1,6))

for num in gen:
    print(num ** 2)

