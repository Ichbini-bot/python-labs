class Ingredient:
    """Models an ingredient including its name and amount - SUPERCLASS"""
    def __init__(self, name, amount):
        self.name = name 
        self.amount = amount

    def __str__(self):
        return f"There are {self.amount} of {self.name}."

    def use(self, use_amount):
        """Reduces the amount of ingredients available"""
        self.amount -= use_amount

    def expire(self):
        """Expires the ingredient item and overrides it"""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

class Spice(Ingredient): 
    """CHILD Class"""

    """since the connection to a class' superclass always exists, we're able to make calls "upwards" the chain through using python's handy super() call."""
    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}")

    """ override: Python sees that the method has same name as in SUPERclass - therefore it will be overwritten"""
    def expire(self):
        if self.name.lower() == "salt":
            print(f"{self.name} never expires. Ask the sea")
        else:
            print(f"oh dear, these {self.name} went bad...")
            self.name = "expired " + self.name

        

carrots = Ingredient("Carrots", 3)
pepper = Spice("Pepper", 20, "spicy")
salt = Spice("Salt", 200, "salty")
print(carrots, pepper, salt)
print(salt.taste, pepper.taste)
print(carrots.taste)

