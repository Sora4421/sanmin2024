# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:29:03 2024

@author: USER
"""

import sqlite3

conn = sqlite3.connect("web.db")

cursor = conn.cursor()
#left 以左邊為主
#inner 兩邊有交集的地方
sql = "select students.name,lesson.lessonname, lesson.score from students left join lesson on students.sid = lesson.sid where lesson.lessonname is null"

cursor.execute(sql)
data = cursor.fetchall() #串列
for row in data :
    for item in row:
        print(item,end="\t")
    print()
