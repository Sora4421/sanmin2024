# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:10:56 2024

@author: USER
"""

'''
1.亂數產生5~100之間可以被5整除的數產生5個且不可重複的值去儲存
2.a.b.c 三邊長，使用者輸入邊長判斷1.是不是三角形2.是三角形是否為直角三角形

'''
import random

# five = []

# while len(five) < 5 :
#     a = random.randint(5,100)
#     if a % 5 == 0 and a not in five:
#         five.append(a)
        
# print(five)

a = int(input("請輸入角度:"))
b = int(input("請輸入角度:"))
c = int(input("請輸入角度:"))

# if a+b > c and b+c > a and c+a > b:
#     print("他是一個三角形")
#     if a*a+b*b == c*c or b*b+c*c == a*a or c*c+a*a == b*b:
#         print("而且他還是一個直角三角形!!")
#     else:
#         print("他只是一個普通的三角形")
    
# else:
#     print("他只是個盧廣仲")
    
    


if a+b > c and b+c > a and c+a > b:
    print("他是一個三角形沒錯")
    if a == b == c:
        print("他是正三角形")
    elif a == b or b == c or c == a:
        print("他是等腰三角形")
    elif a*a+b*b == c*c or b*b+c*c == a*a or c*c+a*a == b*b:
        print("而且他還是一個直角三角形!!")
else:
    print("他還只是個孩子")
