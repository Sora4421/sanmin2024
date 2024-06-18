# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:53:24 2024

@author: USER
"""

def factorial(data,start):
    result = start
    for item in data:
        result *= item
    return result
res = factorial(data=[3,5,7,11,13],start = 1)
print('結果:{:,}'.format(res))