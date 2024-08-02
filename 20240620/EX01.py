# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

fn = "member.csv"
with open(fn,encoding=('utf-8')) as fObj:
    csvReader = csv.reader(fObj)
    data = list(csvReader)


    for row in csvReader:
        print("Row %s =" % csvReader.line_num,row)
        
        for item in row:
            print("item")