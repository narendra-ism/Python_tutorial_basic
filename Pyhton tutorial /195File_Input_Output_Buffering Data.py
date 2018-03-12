# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:20:37 2018

@author: narendra
"""

# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()


# Try to read from the file
print(read_file.read())

read_file.close()

