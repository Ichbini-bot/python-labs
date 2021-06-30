'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width # compared to increase(Cars) - here s a return statement

    def perimeter(self):
        return (self.length + self.width) *2

rect1 = Rectangle(3, 5)
print(rect1.area())
print(rect1.perimeter())

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circum(self):
        return 2 * math.pi * self.radius

circle1 = Circle(3)
print(circle1.area())
print(circle1.circum())

circle2 = Circle(4)
print(circle2.area())
print(circle2.circum())