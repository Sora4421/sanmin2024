# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:06:21 2024

@author: USER
"""
#r 是 read
file = "yahoo.txt"
file_Obj = open(file,encoding="UTF8")
data = file_Obj.read()

file_Obj.close()
print(data)