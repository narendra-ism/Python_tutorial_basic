# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:34:05 2018

@author: narendra
"""

m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  for item in y:
    x.append(item)
  return x  




print(join_lists(m, n))
