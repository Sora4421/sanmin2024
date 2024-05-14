# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 0
num = 0

for i in range(101):
    if i % 2 == 1:
        a += i
    if i % 7 == 0:
        num += i
    if i % 5 == 0 and i % 15 == 0:
        print(i)
print('奇數和:',a)
print('被7整除數:',num)