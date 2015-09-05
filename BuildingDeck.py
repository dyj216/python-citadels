from Building import Building


class BuildingDeck():
	def __init__(self):
		self.deck = []

	def add(self, building):
		# if type(building) != Building:
		# 	raise TypeError("Incorrect type given to deck. Only accepts Building type.")
		self.deck.append(building)

	def get_size(self):
		return len(self.deck)
