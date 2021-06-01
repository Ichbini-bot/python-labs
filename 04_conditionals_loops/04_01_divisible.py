'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

data = int(input("Pls enter a number: "))

if data %3 == 0:
    print("num is divisible by three!")

else:
    print("number is not divisible by 3")