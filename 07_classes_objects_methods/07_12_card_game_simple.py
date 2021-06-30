import random

class Card:

    globalvar = "test"

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank_names[self.rank]} of {self.suit_names[self.suit]}" #of {Card.globalvar} of {self.globalvar}" difference Card.globalvar vs. self.globalvar???


class Deck:
    def __init__(self):
        self.deck = []
        for i in range(4):
            for x in range(13):
                card = Card(i, x)
                self.deck.append(card)

    def __str__(self):
        res = []
        for card in self.deck:
            res.append(str(card))
        return '\n'.join(res)    

    def shuffle(self):
        print("***\n DECK SHUFFLING\n***")
        random.shuffle(self.deck)

    def pop_card(self):
        return self.deck.pop()

    def add_card(self, card):
        self.cards.append(card)

class Hand(Deck):
    def _init__(self):
        self.hand = []

    def move_cards(self, hand):
        for i in range(6):
            hand.add_card(self.pop_card())

deck = Deck()
deck.shuffle()
print(deck)
print("Hand is: ")
print("Hand is: ")
print("Hand is: ")
hand = Hand()
print(hand.move_cards)


'''
deck.pop_card()
print("***\npopping Card\n***")
print(deck)
'''
