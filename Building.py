class Building:
    def __init__(self, name, value, destroyable=True):
        assert type(name) == str
        assert type(value) == int
        assert type(destroyable) == bool
        self.name = name
        self.value = value
        self.destroyable = destroyable

    def __eq__(self, other):
        return True if self.name == other.name else False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "{}, Value: {}".format(self.name, self.value)

    def is_destroyable(self):
        return self.destroyable

    def get_end_value(self):
        return self.value

    def set_destroyable(self, destroyable):
        self.destroyable = destroyable


class YellowBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        Building.__init__(self, name, value, destroyable)


class RedBuilding(object, Building):
    def __init__(self, name, value, destroyable=True):
        Building.__init__(self, name, value, destroyable)


class GreenBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        Building.__init__(self, name, value, destroyable)


class BlueBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        Building.__init__(self, name, value, destroyable)


class PurpleBuilding(Building):
    def __init__(self, name, value, destroyable=True):
        Building.__init__(self, name, value, destroyable)

    def get_end_value(self):
        if self.name == "University" or self.name == "Dragon's Gate":
            return self.value + 2
        else:
            return self.value

if __name__ == '__main__':
    pass
