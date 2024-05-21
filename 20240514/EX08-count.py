# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:45:47 2024

@author: USER
"""

number = list()

while len(number) < 6:
    num = int(input('輸入1~49之間的數:'))
    if 0 < num < 50:
        if number.count(num) == 0:
            number.append(num)
print(number)
        
        