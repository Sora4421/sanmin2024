# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:07:28 2024

@author: USER
"""

print("學生成績系統")

students = []
score = list()

while True:
    q = input("輸入姓名查詢成績:(Q離開系統)")
    if q == 'q' or 'Q':
        break
    
    if students.count(q) == 1:
        ind = students.index(q)
        print("學生:",students[ind],"分數為:",score[ind])
    else:
        ans = input("是否加入此學生?(y/n)")
        if ans.lower() == 'y':
            s = int(input("輸入分數:"))
            students.append(q)
            score.append(s)
            