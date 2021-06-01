'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

user_number = int(input("Pls enter number between 1 and 1000: "))

number = 0

while number != user_number:
    print(number)
    number += 1

print("congrats: your number is: ", number)