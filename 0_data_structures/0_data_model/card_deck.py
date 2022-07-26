import collections
from tokenize import String

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FreshDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spaids diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self) -> None:
        return len(self._cards)

    def __getitem__(self, position: str) -> String:
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FreshDeck()
print(len(deck))