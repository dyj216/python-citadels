import unittest

import Building


class TestBuilding(unittest.TestCase):
    def setUp(self):
        self.tavern = Building.GreenBuilding('Tavern', 1)
        self.university = Building.PurpleBuilding('University', 6)

    def test_set_destroyable_false(self):
        self.assertEqual(self.tavern.is_destroyable(), True)
        self.tavern.set_destroyable(False)
        self.assertEqual(self.tavern.is_destroyable(), False)

    def test_tavern_end_value(self):
        self.assertEqual(self.tavern.get_end_value(), 1)

    def test_university_end_value(self):
        self.assertEqual(self.university.get_end_value(), 8)
