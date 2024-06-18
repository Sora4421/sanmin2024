# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:28:00 2024

@author: USER
"""

file = "yahoo.txt"
with open(file,encoding="UTF8") as fo:
    for line in fo:
        print(line.rstrip())