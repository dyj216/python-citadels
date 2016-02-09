import unittest
import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game.Game()
        self.game.building_deck.initialize_starting_deck()
        self.game.building_deck.shuffle()
        self.game.create_players(6)
        self.game.current_player = self.game.players.pop(0)

    def test_players_numbers(self):
        self.assertEqual(5, len(self.game.players))

    def test_number_of_buildings_after_player_creation(self):
        self.assertEqual(32, self.game.building_deck.get_size())

    def test_dead_building_deck(self):
        self.assertEqual(0, self.game.dead_building_deck.get_size())


class FirstPlayerFirstRound(TestGame):
    def test_first_player_selects_from_two_cards(self):
        cards = [self.game.building_deck.draw_top_card(), self.game.building_deck.draw_top_card()]
        self.game.current_player.take_card(cards.pop())
        self.game.dead_building_deck.add(cards.pop())
        self.assertEqual(1, self.game.dead_building_deck.get_size())
        self.assertEqual(30, self.game.building_deck.get_size())
        self.assertEqual(5, len(self.game.current_player.get_hand_deck()))

    def test_first_player_builds_if_he_can(self):
        building_to_build = None
        starting_gold = self.game.current_player.get_gold()
        for building in self.game.current_player.get_hand_deck():
            if building.value <= starting_gold:
                building_to_build = building
        if building_to_build:
            self.game.current_player.build_building(building_to_build)
            self.assertEqual(1, len(self.game.current_player.get_built_deck()))
            self.assertEqual(self.game.current_player.get_gold(), starting_gold - building_to_build.value)
