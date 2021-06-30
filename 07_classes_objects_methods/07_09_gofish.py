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
        random.shuffle(self.cards)
        
        
#    def shuffle(self):                 Why does this not work?
#        random.shuffle(self.cards)


    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)



class Hand(Deck):

    def __init__(self, label = ""):
        self.cards = []
        self.label = label

hand = Hand("new hand")
print(hand.cards)
print(hand.label)

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)