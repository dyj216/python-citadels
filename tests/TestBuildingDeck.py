import unittest
import copy

import BuildingDeck
import Building


class TestBuildingDeck(unittest.TestCase):
    def setUp(self):
        self.building_deck = BuildingDeck.BuildingDeck()

        self.building_deck.initialize_starting_deck()

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
