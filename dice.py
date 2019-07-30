import random
class Dice:
    vals = [1, 3, 5]

    def roll_dice(self):
        return random.choice(self.vals)
