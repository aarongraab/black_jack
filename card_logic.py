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
    if card['kind'] == "2":
        return 2
    elif card['kind'] == "3":
        return 3
    elif card['kind'] == "4":
        return 4
    elif card['kind'] == "5":
        return 5
    elif card['kind'] == "6":
        return 6
    elif card['kind'] == "7":
        return 7
    elif card['kind'] == "8":
        return 8
    elif card['kind'] == "9":
        return 9
    elif card['kind'] == "10":
        return 10
    elif card['kind'] == "J":
        return 10
    elif card['kind'] == "Q":
        return 10
    elif card['kind'] == "K":
        return 10
    elif card['kind'] == "A":
        return 11
    else:
        print("Error - get_value: No such card type")
        return None

def get_total(hand):
    total = 0
    for card in hand:
        total += get_value(card)
    return total


