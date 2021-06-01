'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = int(input("enter number: "))

for i in range(1, n+1):
    star = i*"*"
    print(star)
