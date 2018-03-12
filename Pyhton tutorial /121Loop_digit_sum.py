# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:14 2018

@author: narendra
"""

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print(x)
    return total
print(digit_sum(123))