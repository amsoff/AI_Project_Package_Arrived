import random
class Dice:
    vals = [1, 2, 3]

    def roll_dice(self):
        return random.choice(self.vals)
