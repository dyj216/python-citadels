import Building
import Player


class Role:
    def __init__(self):
        self.ability_used = False
        self.name = "Role"
        self.value = 0

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return True if (self.value == other.value and self.name == other.name) else False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return True if self.value > other.value else False

    def __lt__(self, other):
        return True if self.value < other.value else False

    def use_ability(self):
        self.ability_used = True

    def use_automatic_ability(self, player):
        pass

    def tax(self, buildings):
        return 0


class Assassin(Role):
    def __init__(self):
        super(Assassin, self).__init__()
        self.name = "Assassin"


class Thief(Role):
    def __init__(self):
        super(Thief, self).__init__()
        self.name = "Thief"


class Mage(Role):
    def __init__(self):
        super(Mage, self).__init__()
        self.name = "Mage"


class King(Role):
    def __init__(self):
        super(King, self).__init__()
        self.name = "King"

    def tax(self, buildings):
        result = 0
        for building in buildings:
            if isinstance(building, Building.YellowBuilding):
                result += 1
        return result

    def use_automatic_ability(self, player):
        self.take_crown(player)

    def take_crown(self, player):
        player.set_place(1)


class Bishop(Role):
    def __init__(self):
        super(Bishop, self).__init__()
        self.name = "Bishop"

    def tax(self, buildings):
        result = 0
        for building in buildings:
            if isinstance(building, Building.BlueBuilding):
                result += 1
        return result

    def use_automatic_ability(self, player):
        self.make_buildings_industructible(player.get_built_buildings())

    def make_buildings_industructible(self, buildings):
        for building in buildings:
            building.destroyable = False


class Merchant(Role):
    def __init__(self):
        super(Merchant, self).__init__()
        self.name = "Merchant"

    def tax(self, buildings):
        result = 0
        for building in buildings:
            if isinstance(building, Building.GreenBuilding):
                result += 1
        return result

    def use_automatic_ability(self, player):
        self.get_extra_gold(player)

    def get_extra_gold(self, player):
        player._gold += 1


class Architect(Role):
    def __init__(self):
        super(Architect, self).__init__()
        self.name = "Architect"

    def use_automatic_ability(self, player):
        self.increase_build_count(player)

    def increase_build_count(self, player):
        player._build_count = 3


class Warlord(Role):
    def __init__(self):
        super(Warlord, self).__init__()
        self.name = "Warlord"

    def tax(self, buildings):
        result = 0
        for building in buildings:
            if isinstance(building, Building.RedBuilding):
                result += 1
        return result
