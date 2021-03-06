class Card:
    """The Card class holds value and suit of certain card"""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.order={"Diamond": 1, "Spade": 2, "Heart": 3, "Club": 4}

    def __repr__(self):
        """Returns the details of the card"""
        if self.value == 11:
            return f'J of {self.suit}'
        if self.value == 12:
            return f'Q of {self.suit}'
        if self.value == 13:
            return f'K of {self.suit}'
        if self.value == 14:
            return f'Ace of {self.suit}'

        return f'{self.suit} {self.value}'

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.order[self.suit]>other.order[other.suit]:
                return True
            return False


    def __eq__(self, other):
        if self.value==other.value and self.suit==other.suit:
            return True
        return False