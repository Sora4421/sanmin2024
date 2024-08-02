# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

conn = sqlite3.connect("web.db")
cursor = conn.cursor()

def add(name,sex,address):
    global conn,cursor
    sql = "insert into students(name,sex,address) values('{}','{}','{}')".format(name,sex,address)
    cursor.execute(sql)
    conn.commit()
    
    
def delete(sid):
    global conn,cursor
    sql = "delete from students where sid = '{}'".format(sid)
    cursor.execute(sql)
    conn.commit()
    
def updata(sid,name,sex,address):
    global conn,cursor
    sql = "update students set name = ?,sex = ?,address = ? where sid = ?"
    cursor.execute(sql,[name,sex,address,sid])
    conn.commit()
    
    

def query():
    global conn,cursor
    sql = "select * from students"
    cursor.execute(sql)
    data = cursor.fetchall() #串列
    for row in data :
        for item in row:
            print(item,end="\t")
        print()

print("學生資料管理")

while True:
    q = input('a => 新增,u => 修改,d => 刪除,list => 列表,q => 離開:')
    
    if q == 'q':
        break
    
    elif q == 'a':
        print('新增學生資料')
        name = input('請輸入姓名:')
        sex = input('請輸入性別(F/M):')
        address = input('請輸入地址:')
        add(name,sex,address)
        query()
        
    elif q == 'u':
        query()
        sid = int(input('請輸入編號:'))
        name = input('請輸入姓名:')
        sex = input('請輸入性別(F/M):')
        address = input('請輸入地址:')
        updata(sid,name,sex,address)
        query()
        
    elif q == 'd':
        query()
        sid = int(input('請輸入編號:'))        
        delete(sid)
        query()
        
    elif q == 'list':
        query()
    else:
        print('查無此代碼')
    