# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:12:00 2024

@author: USER
"""

student = ("John","Man",96,100,61)

name, sex,*score = student
print("姓名:",name)
print("性別:",sex)
print("分數:",score)