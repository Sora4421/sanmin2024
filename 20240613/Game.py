# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:55:26 2024

@author: USER
"""

import random
from Role import Avisder,SworksMan,Dancer

def fight(me,you):
        print(me.getName(),end='')
        me.fight()
        blood = random.randint(0,10)
        n = random.randint(1,5)
        if isinstance(me,Avisder):
            if me.getHp() <= 50:
                me.cure()
                me.setHp(100)
            else:
                me.fight()
        if n == 3:
            print(you.getName(),'Miss')
        else:
            youblood = you.getHp() - blood
            you.setHp(youblood)
            print("{}損失{}血量,目前血量:{}".format(you.getName(),blood,youblood))


if __name__ == '__main__':
    com = list()
    player = list()
    
    com.append(Avisder('司馬老賊',100,90))
    com.append(SworksMan('曹氏宗親會會長',100,81))
    com.append(Dancer('曹老婆',100,60))
    
    player.append(Dancer('周老婆',100,90))
    player.append(SworksMan('十萬經驗大禮包',100,60))
    player.append(Avisder('羽扇綸巾',100,90))
    
    while (len(com) > 0 and len(player) > 0):
        f = random.randint(1,100)
        
        if f % 2 == 0:
            n = random.randint(0,len(com)-1)
            minblood=list()
            for r in player:
                minblood.append(r.getHp())
            selplayer = player[minblood.index(min(minblood))]    
            fight(com[n],selplayer)
            if selplayer.getHp() <= 0:
                player.remove(selplayer)
        else:
            n = random.randint(0,len(player)-1)
            minblood=list()
            for r in com:
                minblood.append(r.getHp())
            selplayer = com[minblood.index(min(minblood))]    
            fight(player[n],selplayer)
            if selplayer.getHp() <= 0:

                com.remove(selplayer)
            
    if len(com) > 0:
        print('電腦 Win')
    else:
        print("玩家 Win")