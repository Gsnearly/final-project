#!/usr/bin/env python 3


def calculate_balance():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()
    starting_money=float(input("Starting money:\t"))
    bet=float(input("Bet amount:"))
    blackjack=round((bet*1.5)+starting_money,2)
    win=round(starting_money+bet,2)
    push=round(starting_money,2)
    lose=round(starting_money-bet,2)
    print("ENDING MONEY FOR A...\nBlackjack:\t",blackjack,"\nWin:\t\t", win,
          "\nPush:\t\t",push,"\nLose:\t\t",lose)
    
    
def main():
    calculate_balance()


if __name__ == "__main__":
    main()
