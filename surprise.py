import random


class Surprise:
    surprises = [-300, -200, -100, 0, 200, 300]
    optimistic_expected_surprise = max(surprises)
    mean_expected_surprise = -100

    def get_surprise(self):
        surprise = random.choice(self.surprises)
        return surprise


