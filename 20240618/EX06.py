# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:44:20 2024

@author: USER
"""


#mkdir 只能做一層
import os

path = os.path.join("c:\\", "good")

# 檢查路徑是否存在
if os.path.exists(path):
    print("路徑存在")
else:
    # 如果路徑不存在，提示是否要建立資料夾
    response = input(f"路徑 {path} 不存在，是否要建立資料夾? (Y/N)")
    
    # 如果用戶輸入 'Y'，則建立資料夾
    if response.upper() == 'Y':
        os.mkdir(path)
        print("資料夾建立成功")
    else:
        print("未建立資料夾")

