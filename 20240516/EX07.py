# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:30:29 2024

@author: USER
"""

msg = "現金{:,}元".format(1000000)

print(msg)

msg="姓名:{:10s}利率:{:.2f}".format('Bill',3.1415926)
print(msg)

msg="姓名:{0:^10s}利率:{1:.2f}".format('Bill',3.1415926)
print(msg)