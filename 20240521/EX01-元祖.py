# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:29:14 2024

@author: USER
"""
#元祖
score = (10,20,30,40)

print(type(score))
print(score[0])
print(score[2])

number = 1,2,3,4
print(number)

item = list(score)
item.append(66)

Newscore = tuple(item)
print(Newscore)