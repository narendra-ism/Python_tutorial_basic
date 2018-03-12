# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:16 2018

@author: narendra
"""

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True
print(is_prime(5))