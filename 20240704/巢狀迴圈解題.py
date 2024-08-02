# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:21:07 2024

@author: USER
"""

data = [1,2,3,4,'a','b','b',1]

temp = list()

for i in data:
    if not (i in temp):
        temp.append(i)
print(temp)