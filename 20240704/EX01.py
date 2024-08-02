# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

conn = sqlite3.connect('web.db')

sql = """
create table students(
    sid integer primary key autoincrement,
    name varchar(30),sex varchar(2),
    address varchar(100))
"""
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()