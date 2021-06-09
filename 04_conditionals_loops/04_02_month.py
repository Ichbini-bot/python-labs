'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
user_input = int(input("pls enter num between 1 to 12: "))

month = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}

if user_input >= 1 and user_input <= 12:
    print(month[user_input])
else:
    print("sry, need a num between 1 to 12")

'''
data = int(input("pls enter num between 1 to 12: "))

if data >= 1 and data <= 12:
    if data == 1:
        print("January")
    if data == 2:
        print("February")
    if data == 3:
        print("March")
    if data == 4:
        print("April")
    if data == 5:
        print("Mai")
    if data == 6:
        print("June")
    if data == 7:
        print("July")
    if data == 8:
        print("August")
    if data == 9:
        print("September")
    if data == 10:
        print("October")
    if data == 11:
        print("November")
    if data == 12:
        print("December")
else:
    print("sry, need a num between 1 to 12")
'''