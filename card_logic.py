import random

class Deck:
    def __init__(self):
        self.suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.kind = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = [{'suit': suit, 'kind': kind} for suit in self.suit for kind in self.kind]


def shuffle(deck):
    random.shuffle(deck.deck)

def deal_card(deck):
    if len(deck.deck) > 0:
        drawn_card = deck.deck.pop()
        return drawn_card
    else:
        print("Error - deal_card: No more remaining cards in the deck")
        return -1

def get_value(card):
    if card['kind'] in ("J", "Q", "K"):
        return 10
    elif card['kind'] == "A":
        return 11
    else:
        return int(card['kind'])

def get_total(hand):
    total = 0
    for card in hand:
        total += get_value(card)
    return total


