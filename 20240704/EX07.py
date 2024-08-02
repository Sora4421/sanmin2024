# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:11:02 2024

@author: USER
"""

import sqlite3

conn = sqlite3.connect('web.db')
cursor = conn.cursor()
sql = "delete from students where sid = 1"

cursor.execute(sql)
conn.commit()
conn.close()