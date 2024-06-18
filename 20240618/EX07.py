# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:16:13 2024

@author: USER
"""

import os

path = os.path.join("c:\\","lcc")

for file in os.listdir("c:\\lcc"):
    print(file)
    f = os.path.join(path,file)
    if os.path.isdir(f):
        print("是目錄")
        
    elif os.path.isfile(f):
        print("是檔案")