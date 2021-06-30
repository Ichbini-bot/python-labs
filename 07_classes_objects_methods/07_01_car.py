'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    # Class variable
    gearbox = "automatic"
    # Instance variable
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.model} is of the year {self.year} and its max speed is {self.max_speed}km/h and has an {self.gearbox}" # why a self for acceleration? because i am on instance level?

    def increase(self, new_speed = 5): # new_speed no need for self, as this is kind a paramter set from the outside. No need by the way to define new variable
        self.max_speed += new_speed # Why is there no return statement needed?
        # return self.max_speed

merc = Car("AMG", 2017, 250)
bmw = Car("M2", 2019, 250)

print(merc.gearbox)
merc.increase()
merc.increase()
bmw.increase()
print(merc)
print(bmw)