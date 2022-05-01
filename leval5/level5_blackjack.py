#!/usr/bin/env python 3
import objects
import random
import time
from objects import deck
from objects import hand
from objects import dealer_hand
from objects import p_points
from objects import d_points
from objects import starting_money

time1 = 0
time2 = 0 
def display_title():
    print("BLACKJACK!\nBlacjack payout is 3:2")
    print()
    objects.Card.get_money()
    
  
def main(deck):
    global time2
    game=True
    replay="y"
    display_title()
    
    while replay=="y":
        objects.Card.get_deck()

        objects.Deck.deal_card(deck)
        while game is True:
            print()
            choice=input("Hit or Stand (hit/stand): ")
            if choice=="hit":
                objects.Hand.add_card(hand)

                
            elif choice=="stand":
                objects.Hand.get_points(hand,dealer_hand)
                
                game=False
        replay=input("Play again? (y/n): ")
        if replay=="y":    
            game=True
            objects.Hand.get_empty_hand(hand,dealer_hand,p_points)
        else:
            break

    time2= time.perf_counter()
    print("Stop time:",time.ctime())
    get_time()
    print("Bye!")
def get_time():
    global time1,time2
    totaltime = round(time2-time1,2)
    print("Elapsed time: ",totaltime,"sec")
if __name__ == "__main__":
    time1 = time.perf_counter()
    main(deck)
