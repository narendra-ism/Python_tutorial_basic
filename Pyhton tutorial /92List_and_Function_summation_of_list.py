# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:23:13 2018

@author: narendra
"""

n = [3, 5, 7]

def total(number):
  result=0
  for item in number:
    result+=item
  return result
print(total(n))