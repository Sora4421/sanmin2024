# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:28:22 2024

@author: USER
"""

'''
break立即跳出當下的迴圈

continue跳下一個敘述，這題跳過換一下問題。
'''

for i in range(100):
    if i == 15:
        break
    if i % 3 == 0:
        continue
    print("i=",i)
    print("平方:",i*i)
print("finish")