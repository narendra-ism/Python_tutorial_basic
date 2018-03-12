# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:27:05 2018

@author: narendra
"""

squares = [x ** 2 for x in range(1, 11)]

print (*(filter(lambda x: x >= 30 and x <= 70, squares)))