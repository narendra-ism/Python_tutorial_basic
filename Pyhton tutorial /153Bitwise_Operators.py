# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:10:16 2018

@author: narendra
"""

shift_right = 0b1100
shift_left = 0b1

# Your code here!

shift_right = shift_right>>2 
shift_left =shift_left<<2

print(bin(shift_right))
print(bin(shift_left))