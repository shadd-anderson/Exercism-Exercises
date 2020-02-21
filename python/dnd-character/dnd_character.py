import random
import math

attributes = {"strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"}


class Character:
    def __init__(self):
        for attribute in attributes:
            rolls = roll_4d6()
            rolls.remove(min(rolls))
            self.__setattr__(attribute, sum(rolls))
        self.__setattr__("hitpoints", modifier(self.constitution) + 10)

    def ability(self):
        return self.__getattribute__(random.choice(list(attributes)))


def roll_d6():
    return random.randint(1, 6)


def roll_4d6():
    return [x for x in map(lambda x: roll_d6(), range(4))]


def modifier(constitution):
    return math.floor((constitution - 10) / 2)
