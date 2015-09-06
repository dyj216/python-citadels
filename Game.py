import Player
import Building


class Game:
    def __init__(self):
        self._players = []

    def get_players(self):
        return self._players

    def create_players(self, number_of_players):
        for n in range(number_of_players):
            starting_deck = [Building.GreenBuilding('Tavern', 1),
                             Building.GreenBuilding('Tavern', 1),
                             Building.GreenBuilding('Temple', 1),
                             Building.GreenBuilding('Chapel', 2)]
            self._players.append(Player.Player("Player-{}".format(n), starting_deck))
