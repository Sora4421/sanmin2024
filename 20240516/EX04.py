# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:47:19 2024

@author: USER
"""

item = [10,20,30,40]

data = item

print(id(item))
print(id(data))

item[0] = 199

print(data)
print(id(data))
print()
x = 10
y = x

score = [99,66,72]
other = [99,66,72]

if x == y:
    print('2者相同')
    
if score == other:
    print('兩者相同')
    
if x is y: #比較記憶體位置
    print('兩者相同')
    
if score is other:
    print('串列相同')
print()
    
n1 = [10,20,30,40]
n2 = []

for i in n1:
    n2.append(i)
    
print(n1)
print(n2)

import copy
#淺複製，用於一維陣列的複製
n3 = copy.copy(n2)
print(n3)
n2[0] = 699
print(n3)


d = [10,20,[1,2,3]]
e = copy.copy(d)

print(e)

d[2][0] = 99
print(d)
print(e)

f = copy.deepcopy(d)
d[2][1] = 699

print(d)
print(f)