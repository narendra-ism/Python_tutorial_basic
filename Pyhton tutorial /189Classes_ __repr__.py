# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:17:57 2018

@author: narendra
"""

class Point3D(object):
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
    
  def __repr__(self):
    return "(%d, %d, %d)"%(self.x,self.y,self.z)
  
my_point=Point3D(1,2,3)
print(my_point)
    