# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:18:03 2024

@author: USER
"""

import datetime

today = datetime.datetime.today()

print(today)
print()

today2 = datetime.date.today()
print(today2)

f = datetime.datetime.strftime(today,"%Y/%m/%d %H:%M:%S")
f2= datetime.datetime.strftime(today,'%y%m%d')

print(f)
print(f2)