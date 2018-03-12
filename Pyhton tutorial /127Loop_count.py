# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:12 2018

@author: narendra
"""

def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count    
print(count("this is is a ama ","i"))