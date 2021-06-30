'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:
    
    #s_system = "solar system"  

    def __init__(self, name, color, moons, special):
        self.name = name
        self.color = color
        self.moons = moons
        self.special = special

    def __str__(self):
        return f"{self.name} has a {self.color} color, has {self.moons} moons and has a {self.special} as a special."



planet = Planet("jupiter", "2", "blabla", "blablü")
print(planet.name)

