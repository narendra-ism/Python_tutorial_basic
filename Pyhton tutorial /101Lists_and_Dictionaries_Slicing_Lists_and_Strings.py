# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:44:46 2018

@author: narendra
"""

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")



print(animals)