from typing import List, Tuple, Dict, Union

class Card:
    """
    Color Table
    0: Yellow
    1: Green
    2: White
    3: Red
    4: Blue
    """
    colors: tuple = ("Orange", "Green", "White", "Red", "Blue")
    idTable: Tuple[str] = (
        "Y1", "Y1", "Y1", "Y2", "Y2", "Y3", "Y3", "Y4", "Y4", "Y5",
        "G1", "G1", "G1", "G2", "G2", "G3", "G3", "G4", "G4", "G5",
        "W1", "W1", "W1", "W2", "W2", "W3", "W3", "W4", "W4", "W5",
        "R1", "R1", "R1", "R2", "R2", "R3", "R3", "R4", "R4", "R5",
        "B1", "B1", "B1", "B2", "B2", "B3", "B3", "B4", "B4", "B5",
    )
    colorWheel: str = "YGWRB"
    lackingColorWheel: Dict[str, str] ={
        "Y": "GWRB",
        "G": "YWRB",
        "W": "YGRB",
        "R": "YGWB",
        "B": "YGWR",
    }

    def __init__(self, cardId: int):
        self.id: int = cardId
        self.color: str = self.idTable[cardId][0]
        self.number: int = int(self.idTable[cardId][1])
        self.short: str = self.idTable[cardId]
        self.hintColor: Dict[str, Union[bool, None]] = {
            # None => unknown
            # True => this card is the color
            # False => this card is not the color
            "Y": None,
            "G": None,
            "W": None,
            "R": None,
            "B": None
        }

    def toShort(self) -> str:
        return self.short

    def getSameColorOnceBefore(self) -> str:
        beforeIdTable = (
            -1, -1, -1, 0, 0, 3, 3, 5, 5, 7,
            -1, -1, -1, 10, 10, 13, 13, 15, 15, 17,
            -1, -1, -1, 20, 20, 23, 23, 25, 25, 27,
            -1, -1, -1, 30, 30, 33, 33, 35, 35, 37,
            -1, -1, -1, 40, 40, 43, 43, 45, 45, 47,
        )
        if self.number == 1:
            return ""
        return Card(cardId=beforeIdTable[self.id]).toShort()

    def __repr__(self):
        return self.toShort()

    def setHint(self, hint: str):
        # if hint is color
        for color in self.lackingColorWheel:
            if self.toShort().startswith(color):
                self.hintColor[color] = True
                for lackColor in self.lackingColorWheel[color]:
                    self.hintColor[lackColor] = False
            else:
                self.hintColor[color] = False
