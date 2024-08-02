# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:27:15 2024

@author: USER
"""

#請用程式寫費式數列 0,1,1,2,3,5,8,13,21,34

#想法1-用串列
#方法2-遞迴

def factorial(n):
    if n == 0 or n ==1: #達成條件才往上傳遞
        return 1
    else:
        return factorial(n-1) * n #直到條件達成前往下傳遞N-1的數值
    
print(factorial(6))

