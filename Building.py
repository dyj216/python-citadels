class Building():
	def __init__(self, name, color, value, destroyable=True):
		self.name = name
		self.color = color.lower()
		self.value = value
		self.destroyable = destroyable

	def __eq__(self, other):
		return True if self.name == other.name else False

	def __ne__(self, other):
		return not self.__eq__(other)

	def is_destroyable(self):
		return self.destroyable

	def get_end_value(self):
		if self.name == "University" or self.name == "Dragon's Gate":
			return self.value + 2
		else:
			return self.value

	def set_destroyable(self, destroyable):
		self.destroyable = destroyable
