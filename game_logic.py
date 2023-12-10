from card_logic import *

deck = Deck()
INITIAL_DEAL = 2
dealer_hand = []
player_hand = []

def initial_setup():
    i = 0
    shuffle(deck)
    while i < INITIAL_DEAL:
        dealer_hand.append(deal_card(deck))
        player_hand.append(deal_card(deck))
        i += 1

def hit_player():
    player_hand.append(deal_card(deck))
def hit_dealer():
    dealer_hand.append(deal_card(deck))

initial_setup()


print("Dealer Hand: ", dealer_hand)
print("Player Hand: ", player_hand)

print("Total for dealer: ", get_total(dealer_hand))
print("Total for player: ", get_total(player_hand))




"""
for card in deck.deck:
    print(get_value(card))
"""
