# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:19:48 2024

@author: USER
"""

file = "yahoo.txt"
with open(file,encoding="UTF8") as fo:
    data = fo.read()
    print(data.rstrip()) #刪除空白
    