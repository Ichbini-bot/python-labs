'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
lower = int(input("pls enter lower number: "))
upper = int(input("pls enter upper number: "))

total = 0

for num in range(lower, upper+1):
    total += num

print(total)