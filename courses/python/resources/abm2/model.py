# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:01:28 2023

@author: Andy Turner
"""
import random
import math
import matplotlib
from matplotlib import pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10

# Initialise agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

# Move agents
for i in range(n_agents):
    # Change agents[i] coordinates randomly
    # x-coordinate
    rn = random.random()
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # y-coordinate
    rn = random.random()
    print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)

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

# Plot
plt.ylim(0, 99)
plt.xlim(0, 99)
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()