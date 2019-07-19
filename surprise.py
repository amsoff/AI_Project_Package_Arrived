import random


class Surprise:
    surprises = [-1000, 200, 500, 350, 0, -350, -210, -240, -280, -90, -10, 300, 20, 55, -120, 350, -50, 2510, -350, 110]

    def get_surprise(self):
        surprise = random.choice(self.surprises)
        return surprise

