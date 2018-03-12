# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:25:53 2018

@author: narendra
"""

languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print(*(filter(lambda x: x == "Python", languages)))