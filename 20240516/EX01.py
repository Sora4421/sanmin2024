# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:49:31 2024

@author: USER
"""

score = [99,89,92,100,62,73]

data = sorted(score)

print('舊資料:',score)
print('排序後:',data)

print(sorted(score,reverse = True))

for i in sorted(score,reverse= True):
    print(i)