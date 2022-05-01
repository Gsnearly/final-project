#!/usr/bin/env python 3
def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit")
    print()
def track_money():
    starting_money=float(input("Starting money:\t"))
    bet=input("Bet amount:")
    while bet!="x":
        bet=int(bet)
        choice=input("Blackjack,win,push, or lose? (b/w/p/l): ")
        if choice=="b":
            blackjack=round((bet*1.5)+starting_money,2)
            starting_money=blackjack
            print("Money:",starting_money)
            bet=input("Bet amount:")
            
        elif choice=="w":
            win=round(starting_money+bet,2)
            starting_money=float(win)
            print("Money:",starting_money)
            bet=input("Bet amount:")
            
        elif choice=="p":
            push=round(starting_money,2)
            starting_money=push
            print("Money:",starting_money)
            bet=input("Bet amount:")
            
        elif choice=="l":
            lose=round(starting_money-bet,2)
            starting_money=lose
            print("Money:", starting_money)
            bet=input("Bet amount:")
    print("Bye!")
    
    
    
def main():
    display_title()
    track_money()
    
    


if __name__ == "__main__":
    main()
