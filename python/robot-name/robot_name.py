import random
from string import ascii_uppercase


class Robot:
    _used_names = set()

    def __init__(self):
        self.reset()

    def reset(self):
        name = ""
        valid_name = False
        while not valid_name:
            for _ in range(2):
                name += random.choice(ascii_uppercase)
            for _ in range(3):
                name += str(random.randint(0, 9))
            if name not in Robot._used_names:
                valid_name = True
                Robot._used_names.add(name)
                self.name = name
            else:
                name = ""
