# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:32:42 2018

@author: narendra
"""

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message=filter(lambda x: x!="X",garbled )
print(*message)