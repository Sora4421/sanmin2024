# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:45:36 2024

@author: USER
"""



class Dancer:
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
    def fight(self):
        print("踢死他")
    def song(self):
        print("使出獅吼攻")
        
    def getName(self):
        return self.__name
    def getHp(self):
        return self.__hp
    def getMp(self):
        return self.mp
    def setHp(self,hp):
        self.__hp = hp
    def setMp(self,mp):
        self.__mp = mp
        
class SworksMan:
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
    def fight(self):
        print("使出西洋劍")
    def Deathblow(self):
        print("屠龍刀")
    def getName(self):
        return self.__name
    def getHp(self):
        return self.__hp

    def setHp(self,hp):
        self.__hp = hp
        
        
class Avisder:
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
    def fight(self):
        print("使出扇子攻擊")
    def cure(self):
        print("全體補血")
    def getName(self):
        return self.__name
    def getHp(self):
        return self.__hp

    def setHp(self,hp):
        self.__hp = hp        
        
        
        
        
        

