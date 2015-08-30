import unittest

import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player.Player("Napoleon")

    def test_player_starting_gold(self):
        self.assertEqual(self.player.get_gold(), 2)

    def test_starting_hand_deck(self):
        self.assertEqual(len(self.player.get_hand_deck()), 4)

    def test_start_player_turn_take_gold(self):
        self.player.take_gold()
        self.assertEqual(self.player.get_gold(), 4)

    def test_start_player_turn_take_card(self):
        self.player.take_card()
        self.assertEqual(len(self.player.get_hand_deck()), 5)
