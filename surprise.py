import random


class Surprise:
    """
    Different amounts of surprises you can win/lose when landing on a surprise cell
    """
    surprises = [-300, -200, -100, 0, 200, 300]
    # surprises = [-300, -200, -100]
    optimistic_expected_surprise = max(surprises)
    avg_player_expected_surprise = -100

    def get_surprise(self):
        surprise = random.choice(self.surprises)
        return surprise


