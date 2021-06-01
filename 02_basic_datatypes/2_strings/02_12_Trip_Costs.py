'''
Receive the following arguments from the user:

kilometers to drive
liters-per-kilometer usage of the car
price per liter of fuel

Calculate the cost of the trip and display it to the user in the console.
'''

km = float(input("Pls enter kilometers to drive: "))
usage = float(input("Pls tell the liters-per-km usage of the car: "))
literprice = float(input("Pls advice on price per liter of fuel: "))

costs = km * usage * literprice
print("Your trip will cost you: ", costs)