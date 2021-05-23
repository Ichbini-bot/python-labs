'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

# Formula for total surface of cylinder: A = 2*Pi*r*h+2*Pi*r^2
# Formula for the volume of the cylinder: V = Pi*r^2*h

# Surface:
pi, height = 3.14, 5
radius = pi # Note: works in this case, as radius = Pi.

surface = 2 * pi * radius * height + 2 * pi * radius**2
print(surface)

#Volume:
volume = pi * radius **2 * height
print(volume) 