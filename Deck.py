import random
import copy
from Card import *

class Deck:
    """
    Cards' Number in the initial deck
    111 22 33 44 5 for each color
    """

    def __init__(self, initial: list=None, _seed:int = None):
        colors: tuple = (0, 1, 2, 3, 4)
        numbers: tuple = (1, 1, 1, 2, 2, 3, 3, 4, 4, 5)
        starter: list = [
                Card(cardId=id)
                for id in range(50)
        ]
        random.seed(_seed)

        if initial:
            self._cards = copy.deepcopy(initial)
            self._drew = []

            # build removed cards list
            for cardInitial in initial:
                for cardStarter in starter:
                    if cardInitial.toShort() == cardStarter.toShort():
                        self._drew.append(cardInitial)
                        # self.remove(cardInitial)

        else:
            self._cards = starter
            self._drew = []

    def reprCards(self):
        shorts = (card.toShort() for card in self._cards)
        result = ""
        for short in shorts:
            result += f'{short} '
        return  result.rstrip()

    def draw(self) -> Card:
        if self.remainCardNum() == 0:
            raise ValueError("no card remain in deck")
        else:
            index: int = random.randint(0, self.remainCardNum()-1)
            drew = self._cards.pop(index)
            self._drew.append(drew)
            return drew

    def remove(self, card: Card) -> Card:
        for num, cardInDeck in enumerate(self._cards):
            if cardInDeck.toShort() == card.toShort():
                return self._cards.pop(num)
        raise ValueError("the card not found tried remove")

    def remainCardNum(self) -> int:
        return len(self._cards)

    def remainCardList(self) -> list:
        return [card for card in self._cards]

    def drewCardList(self) -> list:
        return [card for card in self._drew]