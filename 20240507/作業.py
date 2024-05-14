# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:58:15 2024

@author: USER
"""

'''
題目
1.利用for計算1~100奇數和，要印出
1-1.加總可被7整除的數
1-2.列出同時可被5和15整除的數

2.9*1
9*2
9*3...
2*1
2*2
2*3
'''
totil = 0
a = []
b = []

for i in range(1,101,2):
    totil += i
    if i % 7 == 0:
        a.append(i)
    elif i % 5 == 0 and i % 15 ==0:
        b.append(i)
print("1:",totil)
print("2:",a)
print("3:",b)
print()

for c in range(1,10):
    for d in range(9,1,-1):
        print(d,"*",c,"=",c*d,sep="",end="\t")
    print()

print()

for e in range(9,1,-1):
    for f in range(9,1,-1):
        print(f,"*",e,"=",e*f,sep="",end="\t")
    print()

