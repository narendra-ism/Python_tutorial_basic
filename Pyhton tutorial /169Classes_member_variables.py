# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:14:38 2018

@author: narendra
"""

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health="good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)
    
    
hippo=Animal("dog",15)
sloth=Animal("rat",3)
ocelot=Animal("cat",5)
print(hippo.health)
print(sloth.health)
print(ocelot.health)