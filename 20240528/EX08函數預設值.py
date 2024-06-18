# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:03:04 2024

@author: USER
"""

def circle(r=5):
    print("半徑:",r)
    area = r*r*3.14
    print('圓面積:',area)
circle()
circle(11)
print()

#如果有定義預設值，那後面的參數都要定義預設值
def city(number,name = '台中',parent = '市民'):
    print(number)
    print(name)
    print(parent)
city(400)
city(700,'高雄')
city(900,'台東','原住民')

    