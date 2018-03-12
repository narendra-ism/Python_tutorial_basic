# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:43:22 2018

@author: narendra
"""

print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print (original)
else:
  print ("empty")