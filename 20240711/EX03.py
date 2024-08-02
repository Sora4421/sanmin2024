# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:15:52 2024

@author: USER
"""

import sqlite3

conn = sqlite3.connect('web.db')

cursor = conn.cursor()
sql = """
insert into lesson(sid,lessonname,score) 
values(6,'python',3),(7,'python',3),(8,'C++',4)
"""

cursor.execute(sql)
conn.commit()
conn.close()