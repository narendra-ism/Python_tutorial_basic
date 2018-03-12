# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:32:09 2018

@author: narendra
"""

def flip_bit(number,n):
  mask=0b1<<(n-1)
  result=number^mask
  return bin(result)
print(flip_bit(7,3))