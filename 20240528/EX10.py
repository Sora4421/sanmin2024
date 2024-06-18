# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:40:20 2024

@author: USER
"""

name = ['Bill','Mary','Peter']
score = [92,100,69]
item = zip(name,score)
print(list(item))

for k,v in zip(name,score):
    print(k)
    print(v)