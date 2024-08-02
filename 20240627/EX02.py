# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:11:02 2024

@author: USER
"""

import matplotlib.pyplot as plt

data1 = [12,16,19,36,55,88,90,99]
data2 = [1,2,3,4,5,6,7,8]
data3 = [2,4,6,7,8,9,10,22]
data4 = [4,5,12,18,20,26,27,36]

seq = [1,2,3,4,5,6,7,8]




plt.plot(seq,data1,'-*',seq,data2,'-o',seq,data3,'-^',seq,data4,'-s')
plt.title('Chart')
plt.xlabel('X_Value')
plt.ylabel('Y_Value')
plt.tick_params(axis='both',labelsize=14,color='red')
plt.show()