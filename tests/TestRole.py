import unittest

import Role
import Building
import Player


class TestRole(unittest.TestCase):
    def setUp(self):
        self.starting_deck = [Building.GreenBuilding("Tavern", 1),
                              Building.YellowBuilding("Estate", 3),
                              Building.BlueBuilding("Temple", 1),
                              Building.RedBuilding("Jail", 2)]
        self.player = Player.Player("Napoleon", self.starting_deck)

        self.assassin = Role.Assassin()
        self.thief = Role.Thief()
        self.mage = Role.Mage()
        self.king = Role.King()
        self.bishop = Role.Bishop()
        self.merchant = Role.Merchant()
        self.architect = Role.Architect()
        self.warlord = Role.Warlord()
        self.roles = [self.assassin, self.thief, self.mage, self.king, self.bishop, self.merchant,
                      self.architect, self.warlord]

    def test_use_ability(self):
        for role in self.roles:
            role.use_ability()
            self.assertEqual(role.ability_used, True)

    def test_taxing_king(self):
        self.assertEqual(self.king.tax(self.starting_deck), 1)

    def test_taxing_merchant(self):
        self.assertEqual(self.merchant.tax(self.starting_deck), 1)

    def test_taxing_bishop(self):
        self.assertEqual(self.bishop.tax(self.starting_deck), 1)

    def test_taxing_warlord(self):
        self.assertEqual(self.warlord.tax(self.starting_deck), 1)

    def test_king_automatic_ability(self):
        self.king.use_automatic_ability(self.player)
        self.assertEqual(self.player._place, 1)

    def test_bishop_automatic_ability(self):
        self.bishop.use_automatic_ability(self.player)
        for building in self.player.get_built_buildings():
            self.assertEqual(building.destroyable, False)

    def test_merchant_automatic_ability(self):
        self.merchant.use_automatic_ability(self.player)
        self.assertEqual(self.player.get_gold(), 3)

    def test_architect_automatic_ability(self):
        self.architect.use_automatic_ability(self.player)
        self.assertEqual(self.player._build_count, 3)
