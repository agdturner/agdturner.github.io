# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:34:37 2023

@author: agdtu
"""
import random

class Agent:
    
    def __init__(self, i):
        """
        The constructor method.

        Parameters
        ----------
        i : Integer
            To be unique to each instance.

        Returns
        -------
        None.

        """
        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        pass

    def __str__(self):
        return self.__class__.__name__ + "(x=" + str(self.x) \
            + ", y=" + str(self.y) + ")"

    def __repr__(self):
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        """
        Randomly change x and y.

        Parameters
        ----------
        x_min : Integer
            The minimum x coordinate constraint.
        y_min : TYPE
            The minimum y coordinate constraint.
        x_max : TYPE
            The maximum x coordinate constraint.
        y_max : TYPE
            The maximum y coordinate constraint.

        Returns
        -------
        None.

        """
        # x-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        # y-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            self.y = self.y + 1
        else:
            self.y = self.y - 1
            # Variables for constraining movement.
              # The minimum x coordinate.
              x_min = 0
              # The minimum y coordinate.
              y_min = 0
              # The maximum x coordinate.
              x_max = 99
              # The maximum y coordinate.
              y_max = 99
        # Apply movement constraints.
        if self.x < x_min:
            self.x = x_min
        if self.y < y_min:
            self.y = y_min
        if self.x > x_max:
            self.x = x_max
        if self.y > y_max:
            self.y = y_max



    def getx(self):
        return self._x
        
    def setx(self, x):
        self._x = x
       
    def delx(self):
        del self._x

    #x = property(getx, setx, delx, "I'm the 'x' property.")