# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:10 2018

@author: narendra
"""

def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t
print(anti_vowel("narendra"))