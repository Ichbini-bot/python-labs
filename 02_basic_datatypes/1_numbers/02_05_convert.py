'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
x = 42
y = float(x)
print(y) 
# in this case, no information is lost

x = 40.5
y = int(x)
print(y)
# info loss, as Python rounds the float to the next lower figure (40.5 vs 40) => did expect 41...

x = 3.0 // 2
print(x)
# implicit conversion from int to float. however, from logical point of view not needed as only ints are considered through // operator

num1 = int(input("pls enter number 1: ")) 
num2 = int(input("pls enter number 2: "))
output = num1 * num2
print(output)
# note for me: dont forget to convert input, as per default it is a string and cannot be multiplied!