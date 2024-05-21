# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:59:55 2024

@author: User
"""

import random

def create_deck():
    """創建一副52張牌的撲克牌"""
    deck = [i for i in range(1, 14)] * 4
    random.shuffle(deck)
    return deck

def draw_card(deck):
    """從牌堆中抽取一張牌"""
    card = deck.pop()
    if card > 10:  # J、Q、K為0.5
        return 0.5
    return card

def calculate_score(cards):
    """計算手中所有牌的總點數"""
    return sum(cards)

def ten_half_game():
    player_points = 100
    deck = create_deck()
    
    while True:
        if player_points <= 0:
            print("你已破產！遊戲結束。")
            break
        
        print(f"你目前的點數: {player_points}")
        bet = int(input("請下注: "))
        
        if bet > player_points:
            print("你沒有足夠的點數下注！")
            continue
        
        player_cards = []
        dealer_cards = []
        
        # 玩家和莊家首次抽牌
        player_cards.append(draw_card(deck))  # 修改：起手牌為一張
        dealer_cards.append(draw_card(deck))  # 修改：莊家的起手牌為一張
        
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        
        print(f"你抽到的牌: {player_cards} (總點數: {player_score})")
        print(f"莊家抽到的牌: {dealer_cards} (總點數: {dealer_score})")
        
        # 檢查是否10點半
        if player_score == 10.5 and dealer_score == 10.5:
            print("雙方都是10點半，平手！")
        elif player_score == 10.5:
            print("你得到10點半，贏得雙倍下注點數！")
            player_points += bet * 2
        elif dealer_score == 10.5:
            print("莊家得到10點半，你輸了下注點數！")
            player_points -= bet
        else:
            if player_score <= 10.5:
                # 玩家回合
                while len(player_cards) < 5:
                    choice = input("是否繼續抽牌？(y/n): ").lower()
                    if choice == 'y':
                        player_cards.append(draw_card(deck))
                        player_score = calculate_score(player_cards)
                        print(f"你抽到的牌: {player_cards} (總點數: {player_score})")
                        
                        if player_score == 10.5:
                            print("你得到10點半！")
                            player_points += bet * 2
                            break
                        elif player_score > 10.5:
                            print("你的點數超過10點半，莊家贏了！")
                            player_points -= bet
                            break
                    else:
                        break
                
                if len(player_cards) == 5:
                    print("恭喜你過五關，獲勝！")
                    player_points += bet * 3
                
                if player_score <= 10.5:
                    # 莊家回合
                    while dealer_score < 7.5:
                        dealer_cards.append(draw_card(deck))
                        dealer_score = calculate_score(dealer_cards)
                    
                    print(f"莊家的牌: {dealer_cards} (總點數: {dealer_score})")
                    
                    if dealer_score > 10.5:
                        print("莊家的點數超過10點半，你贏了！")
                        player_points += bet
                    elif dealer_score > player_score:
                        print("莊家贏了！")
                        player_points -= bet
                    elif dealer_score == player_score:
                        print("平手！")
                    else:
                        print("你贏了！")
                        player_points += bet
        
        # 檢查剩餘牌數，重新洗牌
        if len(deck) < 20:
            print("剩餘牌數不足，重新洗牌...")
            deck = create_deck()
        
        # 玩家選擇是否繼續遊戲或退出
        if input("是否繼續遊戲？(y/n): ").lower() == 'n':
            break
    
    print("遊戲結束！")

ten_half_game()

