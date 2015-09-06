import random
import Building


class BuildingDeck:
    def __init__(self):
        self.deck = []

    def __eq__(self, other):
        if len(self.deck) != len(other.deck):
            return False
        for i in range(len(self.deck)):
            if self.deck[i] != other.deck[i]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def add(self, building):
        assert isinstance(building, Building.Building)
        self.deck.append(building)

    def draw_top_card(self):
        return self.deck.pop(0)

    def get_size(self):
        return len(self.deck)

    def shuffle(self):
        temp_deck = []
        while len(self.deck) > 0:
            temp_deck.append(self.deck.pop(random.randint(0, len(self.deck) - 1)))
        self.deck = temp_deck
