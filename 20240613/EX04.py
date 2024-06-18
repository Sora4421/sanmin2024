# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:33:03 2024

@author: USER
"""

file = "yahoo.txt"
with open(file,encoding="UTF8") as fo:
    data = fo.readline()
i=1
for row in data:
    if '立委' in row:
        print('第{}找到'.format(i))
        print(row)
    i += 1