'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
n = 1
for n in range(1, 101):
    if n % 2 != 0:
        print(n)