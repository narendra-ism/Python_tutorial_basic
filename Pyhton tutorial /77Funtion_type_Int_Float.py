# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:19:32 2018

@author: narendra
"""

def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"
  
  
print(distance_from_zero(-4))  