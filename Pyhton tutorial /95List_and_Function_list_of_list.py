# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:38:05 2018

@author: narendra
"""

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results=[]
  for numbers in lists:
    for item in numbers:
      results.append(item)
  return results    



print (flatten(n))