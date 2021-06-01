'''
Print out every prime number between 1 and 100.

'''


for n in range(1, 101):
    prime = True
    for i in range(2,n):
        if (n%i==0):
            prime = False
    if prime == True:
       print(n)