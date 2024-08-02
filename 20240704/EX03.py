# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:03:23 2024

@author: USER
"""

import sqlite3

conn = sqlite3.connect('web.db')

cursor = conn.cursor()

sql = "select * from students"

cursor.execute(sql)

data = cursor.fetchall()
print(data)
for row in data:
    for item in row:
        print(item,end=',')
    print()

conn.close()