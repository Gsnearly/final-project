#!/usr/bin/env python 3
import random 
def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit")
    print()
def track_money():
    starting_money=float(input("Starting money:\t"))
    odd1=.05 # 5% chance for Blackjack
    odd2=.09 # 9% chance for a Push
    odd3=.37 # 37% chance for a win
    odd4=.49 # 49% chance for a loss
    bet=input("Bet amount:")
    while bet!="x":
        bet=int(bet)
        if random.random()<odd1: # random.random() gives a float value between [0.0,1.0]. Here it gives it a 5% chance for a blackjack
            blackjack=round((bet*1.5)+starting_money,2)
            starting_money=blackjack
            print("You got a Blackjack!\nMoney:",starting_money)
            print()
            bet=input("Bet amount:")
            
        elif random.random()<odd3: #Here it gives it a 37% chance for a win
            win=round(starting_money+bet,2)
            starting_money=float(win)
            print("You won.\nMoney:",starting_money)
            print()
            bet=input("Bet amount:")
            
        elif random.random()<odd2: #Here it gives it a 9% chance for a push
            push=round(starting_money,2)
            starting_money=push
            print("You pushed.\nMoney:",starting_money)
            print()
            bet=input("Bet amount:")
            
        elif random.random()<odd4: #Here it gives it a 49% chance for a loss
            lose=round(starting_money-bet,2)
            starting_money=lose
            print("You lost.\nMoney:", starting_money)
            print()
            bet=input("Bet amount:")
    print("Bye!")
    
    
    
def main():
    display_title()
    track_money()
    
    


if __name__ == "__main__":
    main()
