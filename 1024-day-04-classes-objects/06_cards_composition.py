"""
06 - Composition: Objects Made of Objects
A Deck HAS Cards. A Hand HAS Cards. Build big things from small, simple classes.
"""

import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        """Blackjack-style value: number cards are worth their number, J/Q/K = 10, A = 11."""
        if self.rank in ["J", "Q", "K"]:
            return 10
        if self.rank == "A":
            return 11
        return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return str(self)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


class Hand:
    def __init__(self, owner):
        self.owner = owner
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def total(self):
        total = 0
        aces = 0
        for card in self.cards:
            total += card.value()
            if card.rank == "A":
                aces += 1
        while total > 21 and aces > 0:   # an ace can count as 1 instead of 11
            total -= 10
            aces -= 1
        return total

    def __str__(self):
        return f"{self.owner}: {self.cards} = {self.total()}"


deck = Deck()
print(len(deck), "cards in a new deck")
deck.shuffle()

player = Hand("You")
dealer = Hand("Dealer")
for _ in range(2):
    player.add(deck.deal())
    dealer.add(deck.deal())

print(player)
print(dealer)
print(len(deck), "cards left")
