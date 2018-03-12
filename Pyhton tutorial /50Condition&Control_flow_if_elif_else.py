# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 00:11:20 2018

@author: narendra
"""

def greater_less_equal_5(answer):
    if answer> 5 :
        return 1
    elif answer<5:          
        return -1
    else:
        return 0
        
print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))
