# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:01:24 2024

@author: USER
"""

#setdefault是給予KEY，如果有就不再新增

game = {'PS5':17900,'switch':10480}
game.setdefault('XSX',21000)
print(game)

game.setdefault('deck')
print(game)

game.setdefault('PS5',15800)
print(game)