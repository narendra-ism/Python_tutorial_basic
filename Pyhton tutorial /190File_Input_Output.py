# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:20:31 2018

@author: narendra
"""

my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()
