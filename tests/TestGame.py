import unittest
import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game.Game()

    def test_create_players(self):
        self.game.create_players(6)
        self.assertEqual(6, len(self.game.get_players()))
