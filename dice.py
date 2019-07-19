import random
class dice:
    dice = [1, 3, 5]

    def roll_dice(self):
        return random.choice(self.dice)
