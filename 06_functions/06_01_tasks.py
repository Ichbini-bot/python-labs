'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
# take in a number from the user between 1 and 1,000,000,000
# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
# print your new variables to display the results

data = int(input("Pls enter a number: "))

def divisible_or(data):
    return data %4 == 0 or data %7 == 0

def divisible_and(data):
    return data %4 == 0 and data %7 ==0

variable_1 = (divisible_or(data))
variable_2 = (divisible_and(data))

print(variable_1, variable_2)





