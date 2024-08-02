# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:57:28 2024

@author: USER
"""

import sqlite3

conn = sqlite3.connect('web.db')
cursor = conn.cursor()
sql = "update students set address = '台南市國華街一號' where sid = 1"

cursor.execute(sql)
conn.commit()
conn.close()