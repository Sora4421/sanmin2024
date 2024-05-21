# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:06:04 2024

@author: USER
"""

fruits = {'apple':100,'banana':49,'orange':69}

print(fruits['orange'])
#print(fruits['Cherray'])

print(fruits.get('cherray'))

print(fruits.get('cherray','還沒進口'))
print(fruits.get('cherray','想吃自己買'))

