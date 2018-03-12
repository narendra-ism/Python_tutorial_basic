# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:20:34 2018

@author: narendra
"""

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for value in my_list:
  my_file.write(str(value) + "\n")
  
my_file.close()