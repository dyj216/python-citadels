import unittest

from Building import Building


class TestBuilding(unittest.TestCase):
	def setUp(self):
		self.tavern = Building('Tavern', 'Green', 1)

	def test_set_destroyable_false(self):
		self.assertEqual(self.tavern.is_destroyable(), True)
		self.tavern.set_destroyable(False)
		self.assertEqual(self.tavern.is_destroyable(), False)

	def test_tavern_end_value(self):
		self.assertEqual(self.tavern.get_end_value(), 1)

	def test_type(self):
		print(type(self.tavern))