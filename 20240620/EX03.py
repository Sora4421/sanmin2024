# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:39:31 2024

@author: USER
"""

import csv
fn="bike.csv"

with open(fn,'w',encoding="utf-8") as fObj:
    csvWriter = csv.writer(fObj)
    csvWriter.writerow(['sna','sbj','bemp'])
    csvWriter.writerow(['三重路口','10','31'])
    csvWriter.writerow(['總統府','5','88'])
    csvWriter.writerow(['南港展覽','7','12'])