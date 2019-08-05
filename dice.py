import random


class Dice:
    """
    Possible dice values
    """
    values = [1,2,3]

    def roll_dice(self):
        return random.choice(self.values)
