from Player import Player
from Building import Building


class Game:
    def __init__(self):
        self._players = []

    def get_players(self):
        return self._players

    def create_players(self, number_of_players):
        for n in range(number_of_players):
            starting_deck = [Building('Tavern', 'green', 1),
                             Building('Tavern', 'green', 1),
                             Building('Temple', 'blue', 1),
                             Building('Chapel', 'blue', 2)]
            self._players.append(Player("Player-{}".format(n), starting_deck))
