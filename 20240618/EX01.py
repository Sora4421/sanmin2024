# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

file = "lcc.txt"
#W 是複寫
word = "Hello python 第一階"
i = 100

with open (file,'a',encoding ="utf-8") as fObj:
    fObj.write(word+'\n')
    fObj.write(str(i)+'\n')

#串流 stream  B是位元組

