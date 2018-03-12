# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:19:28 2018

@author: narendra
"""

def biggest_number(*args):
  print(max(args))
  return max(args)
    
def smallest_number(*args):
  print (min(args))
  return (min(args))

def distance_from_zero(arg):
  print (abs(arg))
  return (abs(arg))

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)