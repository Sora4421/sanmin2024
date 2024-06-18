# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:14:26 2024

@author: USER
"""

def student(school,**personal):
    print(school,'依學生姓名排序')
    for key in sorted(personal):
        print("%-10s%d"%(key,personal[key]))


    print('-'*30)
    
    up60 = {k:v for k,v in personal.items() if v >= 60}
    c = len(up60)
    print('及格多少人:',c,'人')
    
    
    
student('中一中',Mary = 90,Sue = 81,Bill = 39,John = 61,Eric = 42,Tom=72)