'''
Write a script that demonstrates a try/except/else.

'''
while True:
    try:
        result = float(input("number pls: ")) / float(input("number pls: "))
    except ZeroDivisionError:
        print("Sorry! You are dividing by zero ")
    else:
        print(f"Your answer is: {result}")
        break