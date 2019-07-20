import numpy as np
from enum import Enum


class Nodes_Types(Enum):
    EMPTY = -1
    COURT = 1
    POLICE = 2
    LOTTERY = 3
    TAXES = 4
    HOME_OFFICE = 5
    BARBERSHOP = 6
    GARDEN = 7

    @staticmethod
    def types_dict():
        return list(map(lambda c: c.value, Nodes_Types))


class Board:

    def __init__(self, num_players, starting_point=(0, 0), end_point=()):
        self.board_w = 31
        self.board_h = 23
        self.starting_point = starting_point
        self.num_players = num_players

        self.state = np.full((self.board_h, self.board_w), -1, np.int8)

        self.transition_matrix = np.full((self.board_h, self.board_w), -1, np.int8)

        self.transition_dict = {}

    def init_state(self):
        pass

    def init_transition(self):
        pass

    def init_dict(self):
        pass
