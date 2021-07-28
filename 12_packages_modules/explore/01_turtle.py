'''
"why does numpy not work in venv???????? When I install it not in the venv, then it runs...???? 
=> NEED TO ADJUST THE PYTHON VENV PATH!!!, THEN IT RUNS!"
'''

import numpy as np
import turtle_start as ts

forw = int(input("Pls enter distance in pixels: "))
print(ts.move_turtle(forw))

#---------------------------------------------------

x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

vec1 = np.array([x,y])
vec2 = np.array([-x,-y])

answer1 = ts.add(x,y)
answer2 = ts.mult(x,y)
answer3 = ts.dot(vec1,vec2)

print(answer1)
print(answer2)
print(answer3)

