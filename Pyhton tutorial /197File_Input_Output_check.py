# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:20:39 2018

@author: narendra
"""

with open("text.txt","w") as my_file:
    my_file.write("this is my name")
  
  
if my_file.closed != True:
    my_file.close()
print(my_file.closed)
  