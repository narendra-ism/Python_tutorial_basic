# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:05:38 2018

@author: narendra
"""

def shut_down(s):
  if s=="yes":
    return "Shutting down"
  elif s=="no":
    return "Shutting aborted"
  else:
    return "sorry"
  
print(shut_down("yes"))