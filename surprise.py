import random
from statistics import mean


class Surprise:
    surprises = [-300, -200, -100, 0, 200, 300]
    optimistic_expected_surprise = max(surprises)
    mean_expected_surprise = mean(surprises)

    def get_surprise(self):
        surprise = random.choice(self.surprises)
        return surprise

