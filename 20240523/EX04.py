# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:25:16 2024

@author: USER
"""

students = {'John':40,'Peter':70,'Mary':51,'Eric':43,'Bill':88}

up60 = {k:v for k,v in students.items() if v >= 60}

low60 = {k:v for k,v in students.items() if v < 60}

print('不及格有多少人:',len(low60))

for k,v in low60.items():
    print("%-10s%3d"%(k,v))