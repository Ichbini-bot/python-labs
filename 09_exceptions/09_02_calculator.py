'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

value error
zero division error

'''

while True:
    try:
        num1 = float(input("Pls enter first number: "))
        num2 = float(input("Pls enter second number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break
    except ValueError:
        print("Pls enter a number - not a string")
    except ZeroDivisionError:
        print("you cannot divide by 0")

    


