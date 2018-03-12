# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:20:12 2018

@author: narendra
"""

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
print(censor("this is narendra kumar","is"))