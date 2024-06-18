# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:40:40 2024

@author: USER
"""
#例外處理紀錄
import datetime
import os

def writeLog(error):
    today = datetime.datetime.today()
    file = datetime.datetime.strftime(today,'%Y%m%d')+".log"
    path = os.path.join("C:\\lcc",file)

    with open (path,'a',encoding="utf-8") as fObj:
        time = datetime.datetime.strftime(today,'%H:%M:%S')
        fObj.write(time+"\t")
        fObj.write(error+"\n")


score = [90,80,10,100]

try:
    print(score[0])
    print(score[10])

except Exception as err:
    writeLog(str(err))
print("程式執行完畢")