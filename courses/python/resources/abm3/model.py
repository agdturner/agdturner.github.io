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
import time

# Initialise model
# Set the pseudo-random seed for reproducibility
random.seed(0)
# A variable to store the number of agents
n_agents = 10
# A variable to control the number of iterations
n_iterations = 1000
# The minimum an agents x coordinate is allowed to be.
x_min = 0
# The minimum an agents y coordinate is allowed to be.
y_min = 0
# The maximum an agents x coordinate is allowed to be.
x_max = 99
# The maximum an agents y coordinate is allowed to be.
y_max = 99

def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).
    """
    # Calculate the difference in the x coordinates.
    diff_x = x0 - x1
    # Calculate the difference in the y coordinates.
    diff_y = y0 - y1
    # Square the differences and add the squares
    ssd = (diff_x * diff_x) + (diff_y * diff_y)
    # Calculate the square root
    distance = ssd ** 0.5
    return distance

# Test the distance function
print("Check this is equal to 5:", get_distance(0, 0, 3, 4))

def get_max_distance():
    """
    Calculate and return the maximum distance between all the agents

    Returns
    -------
    max_distance : Number
        The maximum distance betwee all the agents.

    """
    # Loop through and calculate distances
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(len(agents)):
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
    return max_distance

# Initialise agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
#print(agents)

# Print the maximum distance between all the agents
start = time.perf_counter()
print("Maximum distance between all the agents", get_max_distance())
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start)

for ite in range(n_iterations): 
    # Move agents
    for i in range(n_agents):
        # Change agents[i] coordinates randomly
        # x-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[i][0] = agents[i][0] + 1
        else:
            agents[i][0] = agents[i][0] - 1
        # y-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[i][1] = agents[i][1] + 1
        else:
            agents[i][1] = agents[i][1] - 1
        # Keep agents in a rectangular area
        if agents[i][0] < x_min:
            agents[i][0] = x_min
        if agents[i][1] < y_min:
            agents[i][1] = y_min
        if agents[i][0] > x_max:
            agents[i][0] = x_max
        if agents[i][1] > y_max:
            agents[i][1] = y_max
    #print(agents)
    
    # Print the maximum distance between all the agents
    print("Iteration", ite, "Maximum distance between all the agents", get_max_distance())
    
# Plot
#plt.ylim(0, 99)
#plt.xlim(0, 99)
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