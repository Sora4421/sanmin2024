# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:01:56 2024

@author: USER
"""
#轉換的部分是INT，將字串轉換成整數
score = int(input("請輸入分數:"))

if score <= 200:
    print("丁")
elif score <= 400:
    print("丙")
elif score <= 500:
    print("乙")
else:
    print("甲")
    
print("程式執行完畢")