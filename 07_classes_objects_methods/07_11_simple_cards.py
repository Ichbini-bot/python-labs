
import random

class Card:

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for i in self.cards:
            res.append(str(i))
        return '\n'.join(res)

    def shuffle(self):
        print("\n""************shuffling cards************\n" "************shuffling cards************\n" "************shuffling cards************""\n")
        random.shuffle(self.cards)

    def draw_card(self):
        #print("\n" "drawing a card from the deck:")
        #popped_card = self.cards.pop()
        #print("\n" "***************" "\n")
        #print(popped_card)
        return self.cards.pop()

class Player:
    def __init__(self, player_name = ""):
        self.player_name = player_name
        self.player_hand = []

    def draw_card(self, deck):
        print(f"player {self.player_name} is drawing a card: ")
        return self.player_hand.append(Deck.draw_card())



deck = Deck()
print(deck)
deck.shuffle()
print(deck)
deck.draw_card()
print("\n" "***************" "\n")
print(deck)
player = Player("Tobi")
print(player)
