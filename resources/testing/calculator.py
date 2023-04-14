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

    """
    r = decimal.Decimal(0)
    for num in nums:
        r += decimal.Decimal(str(num))
    return float(r)