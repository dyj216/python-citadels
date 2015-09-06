import Building


class Player:
    def __init__(self, name, starting_deck):
        self._name = name
        self._gold = 2
        self._hand_deck = starting_deck
        self._built_deck = []
        self._build_count = 1

    def __eq__(self, other):
        return True if self._name == other._name else False

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_gold(self):
        return self._gold

    def get_hand_deck(self):
        return self._hand_deck

    def take_gold(self):
        self._gold += 2

    def take_card(self, building_card):
        self._hand_deck.append(building_card)

    def build_building(self, building_card):
        assert isinstance(building_card, Building.Building)
        if ((self._gold >= building_card.value) and
                (self._build_count > 0 and building_card.name not in [building.name for building in self._built_deck])):
            self._build_count -= 1
            self._gold -= building_card.value
            self._hand_deck.remove(building_card)
            self._built_deck.append(building_card)
            return True
        else:
            return False

    def tax(self):
        self._gold += 1
