# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:24:19 2020

@author: shri
"""

# File Handling

file = open("MyFile",'w')
file.write("I Love FCS")
file.close()

file =open("MyFile",'r')
read=file.read()
print(read)