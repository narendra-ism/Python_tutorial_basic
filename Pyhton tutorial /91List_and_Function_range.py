# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:20:51 2018

@author: narendra
"""

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print (my_function([0,1,2])) 
