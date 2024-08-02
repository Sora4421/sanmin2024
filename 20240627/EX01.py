# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

data1 = [12,16,19,36,55,88,90,99]
data2 = [1,2,3,4,5,6,7,8]
data3 = [2,4,6,7,8,9,10,22]
data4 = [4,5,12,18,20,26,27,36]

seq = [1,2,3,4,5,6,7,8]




plt.plot(seq,data1,'g--',seq,data2,'r.-',seq,data3,'y:',seq,data4,'k.')
plt.title('Chart')
plt.xlabel('X_Value')
plt.ylabel('Y_Value')
plt.tick_params(axis='both',labelsize=14,color='red')
plt.show()