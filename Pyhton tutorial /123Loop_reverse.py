# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:16 2018

@author: narendra
"""

def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
    
print(reverse("narendra"))