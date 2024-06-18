# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:23:07 2024

@author: USER
"""

n1,n2 = eval(input("請輸入2個數字，用，隔開:"))

try:
    result = n1 / n2
except Exception as e:
    print(e)
    
else:
    print("兩者相除為",result)