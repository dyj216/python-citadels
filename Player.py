class Player:
    def __init__(self, name):
        self._name = name
        self._gold = 2
        self._hand_deck = [None, None, None, None]

    def get_gold(self):
        return self._gold

    def get_hand_deck(self):
        return self._hand_deck

    def take_gold(self):
        self._gold += 2

    def take_card(self):
        self._hand_deck.append(None)
