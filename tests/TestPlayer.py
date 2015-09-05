import unittest

from Player import Player
from Building import Building


class TestPlayerStartingValues(unittest.TestCase):
    def setUp(self):
        starting_deck = [Building('Tavern', 'green', 1),
                         Building('Tavern', 'green', 1),
                         Building('Temple', 'blue', 1),
                         Building('Chapel', 'blue', 2)]
        self.player = Player("Napoleon", starting_deck)

    def test_player_starting_gold(self):
        self.assertEqual(self.player.get_gold(), 2)

    def test_starting_hand_deck(self):
        self.assertEqual(len(self.player.get_hand_deck()), 4)


class TestPlayerTurnChoices(unittest.TestCase):
    def setUp(self):
        starting_deck = [Building('Tavern', 'green', 1),
                         Building('Tavern', 'green', 1),
                         Building('Temple', 'blue', 1),
                         Building('Chapel', 'blue', 2)]
        self.player = Player("Napoleon", starting_deck)

    def test_start_player_turn_take_gold(self):
        self.player.take_gold()
        self.assertEqual(self.player.get_gold(), 4)

    def test_start_player_turn_take_card(self):
        self.player.take_card(Building('Warfield', 'red', 5))
        self.assertEqual(len(self.player.get_hand_deck()), 5)


class TestPlayerBuilding(unittest.TestCase):
    def setUp(self):
        starting_deck = [Building('Tavern', 'green', 1),
                         Building('Tavern', 'green', 1),
                         Building('Temple', 'blue', 1),
                         Building('Chapel', 'blue', 2)]
        self.player = Player("Napoleon", starting_deck)

    def test_build_building(self):
        starting_gold = self.player.get_gold()
        building_to_build = self.player.get_hand_deck()[0]
        self.player.build_building(building_to_build)
        self.assertEqual(len(self.player._built_deck), 1)
        self.assertEqual(len(self.player.get_hand_deck()), 3)
        self.assertEqual(self.player.get_gold(), starting_gold-building_to_build.value)

    def test_build_too_expensive(self):
        too_expensive_building = Building('Warfield', 'red', 5)
        self.player.take_card(too_expensive_building)
        self.assertEqual(self.player.build_building(too_expensive_building), False)

    def test_build_too_much(self):
        building_to_build_1 = self.player.get_hand_deck()[0]
        building_to_build_2 = self.player.get_hand_deck()[2]
        self.player.build_building(building_to_build_1)
        self.assertEqual(self.player.build_building(building_to_build_2), False)

    def test_build_already_built_building(self):
        self.player._build_count = 2
        building_to_build_1 = self.player.get_hand_deck()[0]
        building_to_build_2 = self.player.get_hand_deck()[1]
        self.player.build_building(building_to_build_1)
        self.assertEqual(self.player.build_building(building_to_build_2), False)


class TestPlayerTaxing(unittest.TestCase):
    def setUp(self):
        starting_deck = [Building('Tavern', 'green', 1),
                         Building('Tavern', 'green', 1),
                         Building('Temple', 'blue', 1),
                         Building('Chapel', 'blue', 2)]
        self.player = Player("Napoleon", starting_deck)
        # self.player.role = Merchant()
        tavern = Building('Tavern', 'green', 1)
        self.player.build_building(tavern)

    def test_green_taxing(self):
        self.player.tax()
        self.assertEqual(self.player.get_gold(), 2)
