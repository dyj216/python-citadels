import unittest

from BuildingDeck import BuildingDeck
from Building import Building


class TestBuildingDeck(unittest.TestCase):
	def setUp(self):
		self.building_deck = BuildingDeck()
		self.building_deck.add(Building('Tavern', 'green', 1))
		self.building_deck.add(Building('Market', 'green', 1))
		self.building_deck.add(Building('Dock', 'green', 3))
		self.building_deck.add(Building('Harbor', 'green', 5))

		self.building_deck.add(Building('Temple', 'blue', 1))
		self.building_deck.add(Building('Chapel', 'blue', 2))
		self.building_deck.add(Building('Cathedral', 'blue', 5))
		self.building_deck.add(Building('Monastery', 'blue', 3))

		self.building_deck.add(Building('Warfield', 'red', 5))
		self.building_deck.add(Building('Jail', 'red', 2))

		self.building_deck.add(Building('Estate', 'yellow', 3))
		self.building_deck.add(Building('Castle', 'yellow', 5))

		self.building_deck.add(Building('University', 'purple', 6))

	def test_add_card(self):
		previous_length = self.building_deck.get_size()
		self.building_deck.add(Building('Watchtower', 'Red', 1))
		self.assertEqual(self.building_deck.get_size(), previous_length + 1)
