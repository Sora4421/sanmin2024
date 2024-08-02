# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:41:14 2024

@author: USER
"""

import sqlite3

conn = sqlite3.connect('web.db')

cursor = conn.cursor()
sql = """
insert into students(name,sex,address) 
values('Bill','M','台中市一中街一號')
"""
cursor.execute(sql)

sql = """
insert into students(name,sex,address) 
values('candy','F','台中市2中街一號')
"""

cursor.execute(sql)
conn.commit()
conn.close()