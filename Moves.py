from enum import Enum

class PkmnTypes(Enum):
    NORMAL = 1
    FIRE = 2
    WATER = 3
    GRASS = 4
    ...

class Pokemon():

    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.weakness = self.get_weakness()
        self.ineffective = self.get_ineffective()
        self.immune = self.get_immune()

    def get_weakness(self):
        weaknesses = []
        if PkmnTypes.FIRE in self.types:
            weaknesses.append(PkmnTypes.WATER)
            weaknesses.append(PkmnTypes.ROCK)
            weaknesses.append(PkmnTypes.ROCK)
            weaknesses.append(PkmnTypes.GROUND)
        if PkmnTypes.WATER in self.types:
            weaknesses.append(PkmnTypes.GRASS)
            weaknesses.append(PkmnTypes.ELECTRIC)
        return weaknesses

    def get_resistance(self):
        self.ineffective[]
        ...

    def get_immune(self):
        immune = []
        ...


def get_attack_multiplier(attack_type, pokemon):
    if attack_type in pokemon.immune:
        return 0
    else:
        # It's possible to have a double-weakness or double-resistance
        multiplier = 1.0
        multiplier *= .5**pokemon.ineffective.count(attack_type)
        multiplier *= 2**pokemon.weakness.count(attack_type)
        return multiplier