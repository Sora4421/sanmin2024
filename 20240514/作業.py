# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:54:52 2024

@author: User
"""

"""
課後練習
1-1黑名單：10,15,39 不可以被新增進去




1-2 請使用 random 的方式來自動新增這六個數字




1-3 白名單： 17,41 一定要有
""" 
import random

black = [10,15,39]
white = [17,41]
number = []
number.extend(white)

while len(number) < 6:
    num = random.randint(1, 50)
    
    if num == black:
        break
    
    if number.count(num) == 0:
    
        number.append(num)
    

print(number)

    
    
    










