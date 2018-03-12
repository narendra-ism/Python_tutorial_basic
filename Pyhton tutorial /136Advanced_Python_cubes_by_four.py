# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:13:37 2018

@author: narendra
"""

cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print (cubes_by_four)