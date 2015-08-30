import Player


class Game:
    def __init__(self):
        self._players = []

    def get_players(self):
        return self._players

    def create_players(self, number_of_players):
        for n in range(number_of_players):
            self._players.append(Player.Player("Player-{}".format(n)))
