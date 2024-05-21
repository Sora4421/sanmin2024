# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:19:40 2024

@author: USER
"""

student = {'周子瑜':92,'IU':89}
name = input('輸入姓名:')

if name in student:
    print(name,'的成績:',student[name])
    
else:
    score = int(input('輸入分數:'))
    student[name] = score

print(student)

keys = student.keys()
values = student.values()
print(keys)
print(values)

items = student.items()

print(list(items))

it = list(items)
print(it[0])
print(it[0][0])
print(it[0][1])
print()

for k,v in student.items():
    print(k)
    print(v)
    print()