# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:46:57 2018

@author: narendra
"""

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print ('empty')
    
    
print (new_word)