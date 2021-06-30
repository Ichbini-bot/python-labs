'''
class Ingredient:
  """Models an Ingredient. Currently only carrots!"""
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount

class Shark:
    animal_type = "fish"
    location = "ocean"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        print("user has " + str(followers) + " followers")

sammy = Shark("Sammy", 5)
print(sammy.age)
print(sammy.location)

stevie = Shark("Stevie", 8)

print(stevie.name)

stevie.set_followers(77)

print(stevie.animal_type)
'''
class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def summation(self):
        return self.x + self.y

sum = Point(10, 10)
print(sum)




'''
class Cars:
    def __init__(self, model, year, speed = 0):
        self.model = model
        self.year = year
        self.speed = speed

    def honk_horn(self):
        return f"{self.model}, goes beep beep"

    def accelerate(self, acceleration = 5):
        self.speed += acceleration
        
    def breaking(self, slower = 5):
        self.speed -= slower
        if self.speed <= 0:
            self.speed = 0

toyota = Cars("Toyota", 1980, 50)
print(toyota.speed)
toyota.breaking(5)
print(toyota.speed)
toyota.breaking(40)
print(toyota.speed)
toyota.breaking(20)
print(toyota.speed)
toyota.accelerate(25)
print(toyota.speed)

bentley = Cars("Bentley", 2000)
print(bentley.model)
print(bentley.speed)

bentley.accelerate()
print(bentley.speed)
bentley.breaking()
print(bentley.speed)
bentley.breaking()
print(bentley.speed)

print(bentley.honk_horn())
print(toyota.honk_horn())
'''
class Class1:
    def __init__(self, x):
        self.x = x

class Class2(Class1):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        
    def summation(self):
        return self.x + self.y

b = Class2(10, 5)
print(b.summation())