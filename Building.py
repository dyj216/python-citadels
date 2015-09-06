class Building:
    def __init__(self, name, value, destroyable=True):
        assert type(name) == str
        assert type(value) == int
        assert type(destroyable) == bool
        self.name = name.title()
        self.value = value
        self.destroyable = destroyable

    def __eq__(self, other):
        return True if self.name == other.name else False

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_destroyable(self):
        return self.destroyable

    def get_end_value(self):
        return self.value

    def set_destroyable(self, destroyable):
        self.destroyable = destroyable


class YellowBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        super(YellowBuilding, self).__init__(name, value, destroyable)


class RedBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        super(RedBuilding, self).__init__(name, value, destroyable)


class GreenBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        super(GreenBuilding, self).__init__(name, value, destroyable)


class BlueBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        super(BlueBuilding, self).__init__(name, value, destroyable)


class PurpleBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        super(PurpleBuilding, self).__init__(name, value, destroyable)

    def get_end_value(self):
        if self.name == "University" or self.name == "Dragon's Gate":
            return self.value + 2
        else:
            return self.value
