import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
     
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__=='__main__':
    from random import shuffle
    def set_card(deck, position, card):
        deck._cards[position] = card
    deck = FrenchDeck()
    print(deck[0])
    try:
        shuffle(deck)
        print(deck[:5])
    except TypeError as e:
        print(e)

    # Monkey patching FrenchDeck, dinamicaly injecting __setitem__ method
    FrenchDeck.__setitem__ = set_card
    shuffle(deck)
    print(deck[:5])