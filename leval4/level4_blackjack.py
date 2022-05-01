#!/usr/bin/env python 3
import cards
import random

from cards import deck
from cards import hand
from cards import dealer_hand
from cards import p_points
from cards import d_points
from cards import starting_money
from cards import print_moneyadd
def display_title():
    print("BLACKJACK!\nBlacjack payout is 3:2")
    print()
    cards.get_money()
    

def main(deck):
    game=True
    replay="y"
    display_title()
    
    while replay=="y":
        cards.get_deck()
        cards.deal_card(deck)
        while game is True:
            print()
            choice=input("Hit or Stand (hit/stand): ")
            if choice=="hit":
                cards.add_card(hand)
            elif choice=="stand":
                cards.get_points(hand,dealer_hand)
                game=False
        replay=input("Play again? (y/n): ")
        if replay=="y":    
            game=True
            cards.get_empty_hand(hand,dealer_hand,p_points)
        else:
            break

    
    print("Bye!")
    
if __name__ == "__main__":
    main(deck)
