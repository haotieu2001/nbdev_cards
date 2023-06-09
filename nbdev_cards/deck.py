# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../01_deck.ipynb 3
class Deck:
    "A deck of 52 cards, not including jokers"
    def __init__(self): self.cards = [Card(s, r) for s in range(4) for r in range(1,14)]
    def __len__(self): return len(self.cards)
    def __str__(self): return '; '.join(map(str, self.cards))
    def __contains__(self, card): return card in self.cards
    __repr__=__str__
