'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator. ?????????????
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values. ?????????????

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''
class Car:
    def __init__(self, velocity, horsepower, model):
        self.velocity = velocity
        self.horsepower = horsepower
        self.model = model

    def __str__(self):
        return f"{self.model} has {self.horsepower} hp's and highspeed is {self.velocity}"

    def __add__(self, other):
        total_horsepower = self.horsepower + other.horsepower
        total_velocity = self.velocity + other.velocity
        total_model = self.model + other.model
        return Car(total_velocity, total_horsepower, total_model)

car1 = Car(250, 381, "AMG")
car2 = Car(250, 360, "M2")
car3 = Car(270, 376, "RS3")

print(car1)

car1.velocity += 5

print(car1)
print(car2)
print(car3)

car4 = car1 + car2 + car3
print(car4)