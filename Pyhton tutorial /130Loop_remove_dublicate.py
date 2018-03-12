# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:14 2018

@author: narendra
"""

def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    

    inputlist = sorted(inputlist)
    outputlist = [inputlist[0]]


    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
print(remove_duplicates([1,2,3,4,2,2,2,2,4,4,4,5,6,7,8]))