# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:46:57 2023

@author: Andy Turner
"""
import decimal

def add(*nums):
    """
    A function to add numbers.

    Parameters
    ----------
    *nums : Numbers
        The numbers to add.
    
    Returns
    -------
    float
        The sum of all nums.

    >>> add(1, 2)
    3.0
    >>> add(0.1, 0.1, 0.1)
    0.3
    
    """
    r = decimal.Decimal(0)
    for num in nums:
        r += decimal.Decimal(str(num))
    return float(r)

if __name__ == '__main__':
    import doctest
    doctest.testmod()