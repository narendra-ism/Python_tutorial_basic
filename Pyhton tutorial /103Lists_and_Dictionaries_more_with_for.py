# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:45:36 2018

@author: narendra
"""

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for item in start_list:
  square_list.append(item**2)

square_list.sort()

print(square_list)