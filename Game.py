import Player
import Building
import BuildingDeck


class Game:
    def __init__(self):
        self.players = []
        self.building_deck = BuildingDeck.BuildingDeck()
        self.dead_building_deck = BuildingDeck.BuildingDeck()
        self.current_player = None

    def create_players(self, number_of_players):
        for n in range(number_of_players):
            starting_deck = [self.building_deck.draw_top_card(),
                             self.building_deck.draw_top_card(),
                             self.building_deck.draw_top_card(),
                             self.building_deck.draw_top_card()]
            self.players.append(Player.Player("Player-{}".format(n), starting_deck))
