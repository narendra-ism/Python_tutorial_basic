# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:01:46 2018

@author: narendra
"""

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)
hippo=Animal("dog",23)
hippo.description()