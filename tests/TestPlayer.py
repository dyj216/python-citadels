import unittest

import Player
import Building


class TestPlayerStartingValues(unittest.TestCase):
    def setUp(self):
        starting_deck = [Building.GreenBuilding('Tavern', 1),
                         Building.GreenBuilding('Tavern', 1),
                         Building.BlueBuilding('Temple', 1),
                         Building.BlueBuilding('Chapel', 2)]
        self.player = Player.Player("Napoleon", starting_deck)

    def test_player_starting_gold(self):
        self.assertEqual(self.player.get_gold(), 2)

    def test_starting_hand_deck(self):
        self.assertEqual(len(self.player.get_hand_deck()), 4)


class TestPlayerTurnChoices(TestPlayerStartingValues):
    def test_start_player_turn_take_gold(self):
        self.player.take_gold()
        self.assertEqual(self.player.get_gold(), 4)

    def test_start_player_turn_take_card(self):
        self.player.take_card(Building.RedBuilding('Warfield', 3))
        self.assertEqual(len(self.player.get_hand_deck()), 5)


class TestPlayerBuilding(TestPlayerStartingValues):
    def test_build_building(self):
        starting_gold = self.player.get_gold()
        building_to_build = self.player.get_hand_deck()[0]
        self.player.build_building(building_to_build)
        self.assertEqual(len(self.player._built_deck), 1)
        self.assertEqual(len(self.player.get_hand_deck()), 3)
        self.assertEqual(self.player.get_gold(), starting_gold-building_to_build.value)

    def test_build_too_expensive(self):
        too_expensive_building = Building.RedBuilding('Warfield', 3)
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


class TestPlayerTaxing(TestPlayerStartingValues):
    def test_green_taxing(self):
        tavern = Building.GreenBuilding('Tavern', 1)
        self.player.build_building(tavern)
        self.player.tax()
        self.assertEqual(self.player.get_gold(), 2)
