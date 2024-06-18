# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:23:34 2024

@author: USER
"""

def total(*value):
    t = 0
    for i in value:
        t += i
    return t

print(total())
print(total(1,2,3,4))
print(total(10,20))