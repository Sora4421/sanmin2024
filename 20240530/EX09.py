# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:11:33 2024

@author: USER
"""

def divfun(num1,num2):
    try:
        result = divmod(num1,num2)
    except:
        print("捕獲error")
    else:
        print(result)
    finally:
        print("計算完成")
        
divfun(10,5)
divfun(10,0)