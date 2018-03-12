# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:51:35 2018

@author: narendra
"""

def cube(number):
  return number**3
def by_three(number):
  if number%3 == 0:
    return cube(number)
  else:
    return False