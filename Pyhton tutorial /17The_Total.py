# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 17:50:51 2018

@author: narendra
"""

# Assign the variable total on line 8!

meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal * tax
total=meal+meal*tip
print("%.2f" % total)