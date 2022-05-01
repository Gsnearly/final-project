#!/usr/bin/env python 3
import random

deck = []
hand=[]
dealer_hand=[]
p_points=0
d_points=0
starting_money = 0
bet_amount = 0
class Card:
    def get_money():
        global starting_money
        starting_money = int(input("Starting money:\t"))
        print()
        return starting_money
    def get_deck():
        card_rank =['A','K','Q','J',2,3,4,5,6,7,8,9,10]
        card_suits =['Hearts','Clubs','Diamonds','Spades']
        for suits in range(len(card_suits)):
            for ranks in range (len(card_rank)):
                ls=[]
                ls.append(card_suits[suits])
                ls.append((card_rank[ranks]))
                if card_rank[ranks]=="J" or card_rank[ranks]=="Q" or card_rank[ranks]=="K" or card_rank[ranks]==10:
                    ls.append(10)
                    
                elif card_rank[ranks]=="A":
                   ls.append(1)
                        
                elif card_rank[ranks] == 2:
                    ls.append(2)
                    
                elif card_rank[ranks]==3:
                    ls.append(3)
                    
                elif card_rank[ranks] == 4:
                    ls.append(4)
                elif card_rank[ranks] == 5:
                    ls.append(5)
                    
                elif card_rank[ranks] == 6:
                    ls.append(6)
                    
                elif card_rank[ranks]== 7:
                    ls.append(7)
                    
                elif card_rank[ranks]== 8:
                    ls.append(8)
                    
                elif card_rank[ranks] == 9:
                    ls.append(9)
                
                deck.append(ls)
class Deck:
    def shuffle(deck):
        random.shuffle(deck)
    def deal_card(deck):
        global bet_amount
        random.shuffle(deck)
        bet_amount= int(input("Bet amount:"))
        print("DEALERS HAND")
        print()
        for i in range(2):
            dealer_play=[deck[i][0],deck[i][1],deck[i][2]]
            dealer_hand.append(dealer_play)
        print(dealer_hand[0][1], "of" ,dealer_hand[0][0])
        print("YOUR CARDS: ")
        print()
        
        random.shuffle(deck)
        for i in range(2):
            play=[deck[i][0],deck[i][1],deck[i][2]]
            hand.append(play)
            print(deck[i][1], "of",deck[i][0])
        
class Hand:      
    def get_empty_hand(hand,dealer_hand,p_points):
        hand.clear()
        dealer_hand.clear()
        p_points == 0
    def add_card(hand):
        shuffle(deck)
        for i in range (1):
            addc=[deck[i][0],deck[i][1],deck[i][2]]
            hand.append(addc)
            addc=[]
        print()
        print("YOUR CARDS: ")
        for i in range(len(hand)):
            print(hand[i][1], "of", hand[i][0])

    def get_points(hand,dealer_hand):
        p_points=0
        global starting_money
        for i in range(len(hand)):
            p_points+=hand[i][2]


        d_points=dealer_hand[0][2]+dealer_hand[1][2]
        i=2
        print()
        print("DEALER'S CARDS:")
        print(dealer_hand[0][1], "of", dealer_hand[0][0])
        print(dealer_hand[1][1], "of", dealer_hand[1][0])
        while d_points<17:
          addc=[deck[i][0],deck[i][1],deck[i][2]]
          dealer_hand.append(addc)
          print(dealer_hand[i][1], "of", dealer_hand[i][0])
          d_points+=dealer_hand[i][2]
          i=i+1
          break    
            
        print()
        print("YOUR SCORE: ",p_points)
        print()
        print("DEALER SCORE: ",d_points)
        
        if (p_points > d_points) and p_points<=21:
            print("Hooray! You win!")
            Points.moneyadd()
            print()
        elif(p_points < d_points) and d_points<=21:
            print("You lost. The Dealer wins!")
            Points.moneysub()
            print()
            print()
        elif p_points==d_points:
            print("It's a Push!")
            print("MONEY: ",starting_money)
            print()
        elif d_points>21:
            print("Hooray! You win!")
            Points.moneyadd()
            print()
        elif p_points>21:
            print("You lost. The Dealer wins!")
            Points.moneysub()
            print()
class Points:            
    def moneyadd():
        global starting_money,bet_amount
        starting_money = starting_money + bet_amount
        print("MONEY: ",starting_money)
    def moneysub():
        global starting_money,bet_amount
        starting_money = starting_money - bet_amount
        print("MONEY: ",starting_money)

    
            
    


