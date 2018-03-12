# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:13 2018

@author: narendra
"""

def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res
print(purify([1,2,3,4,5,6,7]))