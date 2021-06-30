import random

class Card:
    
    """mapping from the integer codes to the corresponding ranks and suits. CLASS attributes"""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', #None is a place-keeper, because there is no card with rank zero
              '8', '9', '10', 'Jack', 'Queen', 'King']
    
    """Represents a standard playing card. INSTANCE attributes"""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],  #slicing! f.e.: 2, 11 means Jack of Hearts => impressive!!! 
                             Card.suit_names[self.suit])  #use the attribute rank from the object self as an index into the list rank_names from the class Card, and select the appropriate string."""

card1 = Card(2,11)
print(card1)

'''  
    """One has to decide whether rank or suit is more important. To keep things simple, we’ll make the arbitrary choice that suit is more important"""
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4): #The outer loop enumerates the suits from 0 to 3
            for rank in range(1, 14): #The inner loop enumerates the ranks from 1 to 13. Each iteration creates a new Card with the current suit and rank, and appends it to self.cards
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res) #Even though the result appears on 52 lines, it is one long string that contains newlines.

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    # As an exercise, write a Deck method named sort that uses the list method sort to sort the cards in a Deck. sort uses the __lt__ method we defined to determine the order.

class Hand(Deck):
    """Represents a hand of playing cards."""
    """This definition indicates that Hand inherits from Deck; that means we can use methods like pop_card and add_card for Hands as well as Decks."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

hand = Hand("new_hand")
print(hand.cards)
print(hand.label)

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)
'''