# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:36:51 2024

@author: USER
"""

import sqlite3

conn = sqlite3.connect('web.db')

cursor = conn.cursor()

sql = "select name,sex from students where sex = 'M'"

cursor.execute(sql)

data = cursor.fetchall()
print(data)
for row in data:
    for item in row:
        print(item,end=',')
    print()

conn.close()