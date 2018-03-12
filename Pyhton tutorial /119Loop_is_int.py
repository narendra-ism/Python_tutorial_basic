# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:10 2018

@author: narendra
"""

def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False
        
print(is_int(-10))