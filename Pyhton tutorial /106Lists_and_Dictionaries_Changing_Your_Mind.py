# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:48:11 2018

@author: narendra
"""

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
del zoo_animals['Rockhopper Penguin']
zoo_animals['Rockhopper Penguin']="duck"
print(zoo_animals)