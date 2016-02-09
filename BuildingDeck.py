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

    def initialize_starting_deck(self):
        for i in range(5):
            self.add(Building.GreenBuilding("Tavern", 1))
        for i in range(4):
            self.add(Building.GreenBuilding("Market", 2))
        for i in range(3):
            self.add(Building.GreenBuilding("Merchant's House", 2))
            self.add(Building.GreenBuilding("Dock", 3))
            self.add(Building.GreenBuilding("Port", 4))
        for i in range(2):
            self.add(Building.GreenBuilding("Town Hall", 5))

        for i in range(3):
            self.add(Building.BlueBuilding("Temple", 1))
            self.add(Building.BlueBuilding("Chapel", 2))
            self.add(Building.BlueBuilding("Monastery", 3))
        for i in range(2):
            self.add(Building.BlueBuilding("Cathedral", 5))

        for i in range(3):
            self.add(Building.RedBuilding("Sentry Tower", 1))
            self.add(Building.RedBuilding("Jail", 2))
            self.add(Building.RedBuilding("Warfield", 3))
        for i in range(2):
            self.add(Building.RedBuilding("Stronghold", 5))

        for i in range(5):
            self.add(Building.YellowBuilding("Estate", 3))
        for i in range(4):
            self.add(Building.YellowBuilding("Castle", 4))
        for i in range(3):
            self.add(Building.YellowBuilding("Palace", 5))

        self.add(Building.PurpleBuilding("University", 6))
        self.add(Building.PurpleBuilding("Dragon's Gate", 6))

    def draw_top_card(self):
        return self.deck.pop(0)

    def get_size(self):
        return len(self.deck)

    def shuffle(self):
        temp_deck = []
        while len(self.deck) > 0:
            temp_deck.append(self.deck.pop(random.randint(0, len(self.deck) - 1)))
        self.deck = temp_deck
