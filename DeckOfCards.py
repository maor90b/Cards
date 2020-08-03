from Game_Card2.Card import Card
from random import shuffle


class DeckOfCards:
    """The DeckOfCards class holds a deck(list) of cards"""

    def __init__(self):
        self.deck = []
        values = [i for i in range(2, 15)]
        suits = ['Diamond', 'Spade', 'Heart', 'Club']
        for i in values:
            for j in suits:
                self.deck.append(Card(j, i))

        for i in self.deck:
            if type(i) != Card:
                self.deck.remove(i)

    # def __repr__(self):
    #     return f'deck= {self.deck}'

    def __shuffle(self):
        """Shuffle the deck"""
        shuffle(self.deck)

    def deal_one(self):
        """Returns and remove the last card from the deck"""
        if 0 < len(self.deck) <= 52:
            return self.deck.pop()

    def new_game(self):
        """Renew the deck, and shuffle it"""
        self.__init__()
        self.__shuffle()

    def show(self):
        """Print the deck"""
        print(self.deck)
