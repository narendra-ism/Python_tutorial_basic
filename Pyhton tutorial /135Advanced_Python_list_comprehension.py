# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:12:26 2018

@author: narendra
"""

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]


even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print(even_squares)