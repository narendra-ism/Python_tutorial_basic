# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:23:42 2018

@author: narendra
"""

my_list = range(16)
print (*(filter(lambda x: x % 3 == 0, my_list)))