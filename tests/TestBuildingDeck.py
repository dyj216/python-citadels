import unittest
import copy

import BuildingDeck
import Building


class TestBuildingDeck(unittest.TestCase):
    def setUp(self):
        self.building_deck = BuildingDeck.BuildingDeck()

        for i in range(5):
            self.building_deck.add(Building.GreenBuilding("Tavern", 1))
        for i in range(4):
            self.building_deck.add(Building.GreenBuilding("Market", 2))
        for i in range(3):
            self.building_deck.add(Building.GreenBuilding("Merchant's House", 2))
            self.building_deck.add(Building.GreenBuilding("Dock", 3))
            self.building_deck.add(Building.GreenBuilding("Port", 4))
        for i in range(2):
            self.building_deck.add(Building.GreenBuilding("Town Hall", 5))

        for i in range(3):
            self.building_deck.add(Building.BlueBuilding("Temple", 1))
            self.building_deck.add(Building.BlueBuilding("Chapel", 2))
            self.building_deck.add(Building.BlueBuilding("Monastery", 3))
        for i in range(2):
            self.building_deck.add(Building.BlueBuilding("Cathedral", 5))

        for i in range(3):
            self.building_deck.add(Building.RedBuilding("Sentry Tower", 1))
            self.building_deck.add(Building.RedBuilding("Jail", 2))
            self.building_deck.add(Building.RedBuilding("Warfield", 3))
        for i in range(2):
            self.building_deck.add(Building.RedBuilding("Stronghold", 5))

        for i in range(5):
            self.building_deck.add(Building.YellowBuilding("Estate", 3))
        for i in range(4):
            self.building_deck.add(Building.YellowBuilding("Castle", 4))
        for i in range(3):
            self.building_deck.add(Building.YellowBuilding("Palace", 5))

        self.building_deck.add(Building.PurpleBuilding("University", 6))
        self.building_deck.add(Building.PurpleBuilding("Dragon's Gate", 6))

    def test_starting_deck(self):
        self.assertEqual(self.building_deck.get_size(), 56)

    def test_add_card(self):
        new_deck = BuildingDeck.BuildingDeck()
        new_deck.add(Building.GreenBuilding("Tavern", 1))

    def test_shuffle_building_deck(self):
        before_shuffle = copy.copy(self.building_deck)
        self.building_deck.shuffle()
        self.assertNotEqual(before_shuffle, self.building_deck)

    def test_draw_top_card(self):
        self.building_deck.shuffle()
        at_top_card = self.building_deck.deck[0]
        previous_size = self.building_deck.get_size()
        top_card = self.building_deck.draw_top_card()
        self.assertEqual(at_top_card, top_card)
        self.assertEqual(self.building_deck.get_size(), previous_size - 1)
