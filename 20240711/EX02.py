# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

conn = sqlite3.connect('web.db')

sql = """
create table lesson(
    id integer primary key autoincrement,
    sid int,
    lessonname varchar(50),
    score int)
"""
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()