# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:01:28 2023

@author: Andy Turner
"""
import random
import math

nickname = {"thomas": "tom", "samuel": "sam", "samson": "sam"}
alias = dict([("rm", "remove"), ("cd", "change directory"), ("ls", "list")])
print(alias.get("rm")) # <-- This should print 'remove'.

a = (True, False)
print(any(a))
# Set the pseudo-random seed for reproducibility
random.seed(0)
# Initialise variable x0
x0 = 0
print("x0", x0)
# Initialise variable y0
y0 = 0
print("y0", y0)
# Change x0 and y0 randomly
rn = random.random()
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)
# Initialise variable x1
x1 = 0
print("x1", x1)
# Initialise variable y1
y1 = 0
print("y1", y1)
# Change x1 and y1 randomly
rn = random.random()
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1", x1)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1", y1)
# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4
# Calculate the difference in the x coordinates.
diff_x = x0 - x1
# Calculate the difference in the y coordinates.
diff_y = y0 - y1
# Square the differences and add the squares
ssd = (diff_x * diff_x) + (diff_y * diff_y)
print("ssd", ssd)
# Calculate the square root
distance = ssd ** 0.5
print("distance", distance)
distance = math.sqrt(ssd)
print("distance", distance)
