# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:05:16 2024

@author: USER
"""

import random

ans = random.randint(1,100)
guess = 0
count = 1


while ans != guess and count < 4:
    guess = int(input("輸入1~100:"))
    count += 1
    # if count == 4:
    #     break
        
    if guess > ans :
        print("小一點")
    elif guess < ans :
        print("大一點")
    else:
        print("恭喜中獎")
        break
    
if guess == ans:
    print("good")
    
else:
    print("達到次數")