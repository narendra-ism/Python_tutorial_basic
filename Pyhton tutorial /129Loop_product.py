# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:13 2018

@author: narendra
"""


def product(numbers):
    prod = 1
    for num in numbers:
        prod = prod*num
    return prod
    
print(product([4,6,2,6,87,34]))