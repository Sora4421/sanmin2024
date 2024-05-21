# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:51:19 2024

@author: USER
"""

import random

number = list()

while len(number) != 5:
    n = random.randrange(5,101,5)
    if number.count(n) == 0:
        number.append(n)
        
print(number)