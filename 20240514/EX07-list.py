# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:57:57 2024

@author: USER
"""
#計算裡面有幾個
words = ['a','b','c','d','a','c','f']

a = words.count('a')
f = words.count('f')
g = words.count('g')

print('a有:',a)
print('f有:',f)
print('g有:',g)

ind = words.index("d")
print(ind)

#搜尋記數
start = 0
for i in range(words.count('c')):
    ind = words.index('c',start)
    print('C的索引:',ind)
    start = ind + 1