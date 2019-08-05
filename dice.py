import random


class Dice:
    """
    Possible dice values
    """
    values = [2]

    def roll_dice(self):
        return random.choice(self.values)
