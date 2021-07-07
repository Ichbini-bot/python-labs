'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

while loop

'''

while True:
    try:
        integer = int(input("Pls enter an integer number: "))
        print(f"You entered the number {integer}")
        break
        
    except ValueError:
        print("Pls enter an Integer - wether a string nor a float")

