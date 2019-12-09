from typing import List, Type
from Card import *
from Field import *
from Deck import *


class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def __repr__(self):
        result: str = "["
        for card in self.cards:
            result += f'{card.toShort()} '
        return f'{result.rstrip()}]'


class Play:
    def __init__(self):
        self.card: Card = None
        self.cardIndex: int = None
        self.playerID: int = None
        self.hint: str = None


class PlayCard(Play):
    def __init__(self, card: Card, cardIndex: int):
        super().__init__()
        self.card = card
        self.cardIndex = cardIndex


class TrashCard(Play):
    def __init__(self, card: Card, cardIndex: int):
        super().__init__()
        self.card = card
        self.cardIndex = cardIndex


class Hint(Play):
    def __init__(self, playerID: int, hint: str):
        super().__init__()
        self.playerID = playerID
        self.discovered = hint


class Player:
    def __init__(self, id: int, hand: Hand, playerAI):
        self.id = id
        self.hand = hand
        self.playerAI = playerAI

    def guess(self, field: Field, otherPlayerCoveredHands: List[Hand]) -> Play:
        """determine the player how plays."""
        return self.playerAI.guess(player=self, field=field, otherPlayerCoveredHands=otherPlayerCoveredHands)

    def draw(self, deck: Deck):
        """draw a card from the deck."""
        self.hand.cards.append(deck.draw())

    def playCard(self, index: int):
        """attempt put a card to the field."""
        return self.hand.cards.pop(index)

    def hinted(self, hint: str):
        """check hint to the player's hand.
        example:
            hint => "A", "1"
        """
        for card in self.hand.cards:
            card.setHint(hint)

    def trash(self, cardIndex: int, field: Field, deck: Deck):
        """put a card in trash and draw a card."""
        field.trash.append(self.hand.cards.pop(cardIndex))
        self.draw(deck)
