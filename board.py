import numpy as np
from enum import Enum

JUMP = 'jump'
PAY = 'pay'
ONE = 1
THREE = 3
FIVE = 5


class Nodes_Types(Enum):
    EMPTY = -1
    COURT = 1
    POLICE = 2
    LOTTERY = 3
    TAXES = 4
    HOME_OFFICE = 5
    BARBERSHOP = 6
    GARDEN = 7

    ORANGE = 8
    SURPRISE = 9

    @staticmethod
    def types_dict():
        return list(map(lambda c: c.value, Nodes_Types))


class Board:

    def __init__(self, num_players, starting_point=(1, 0), end_point=(21, 27)):
        self.board_w = 23
        self.board_h = 31
        self.starting_point = starting_point
        self.num_players = num_players

        self.state = np.full((self.board_h, self.board_w), -1, np.int8)

        self.transition_matrix = np.full((self.board_h, self.board_w), -1, np.int8)

        self.transition_dict = {}
        self.init_dict()

    def init_state(self):
        pass

    def init_transition(self):
        pass

    def init_dict(self):
        self.init_row0()
        self.init_row1()
        self.init_row2()
        self.init_row3()
        self.init_row4()
        self.init_row5()
        self.init_row6()
        self.init_row7()
        self.init_row8()
        self.init_row9()
        self.init_row10()
        self.init_row11()
        self.init_row12()
        self.init_row13()
        self.init_row14()
        self.init_row15()
        self.init_row16()
        self.init_row17()
        self.init_row18()
        self.init_row19()
        self.init_row20()
        self.init_row21()
        self.init_row22()

    def init_row22(self):
        self.transition_dict[(22, 30)] = {1: [(22, 29)], 3: [(22, 29)], 5: [(22, 29)], JUMP: [(22, 28)]}
        self.transition_dict[(22, 29)] = {1: [(21, 29)], 3: [(21, 29)], 5: [(21, 29)], JUMP: [(22, 27)]},
        self.transition_dict[(22, 28)] = {1: [(22, 27), (21, 28)], 3: [(21, 26), (19, 28)],
                                          5: [(21, 24), (20, 25), (17, 28)]}
        self.transition_dict[(22, 27)] = {1: [(21, 27)], 3: [(21, 25), (20, 28)], 5: [(18, 28), (19, 25), (21, 22)]}
        self.transition_dict[(22, 26)] = {1: [(21, 26)], 3: [(21, 28), (20, 25), (21, 24), (22, 27)],
                                          5: [(19, 28), (19, 25), (21, 22)]}
        self.transition_dict[(22, 25)] = {1: [(222, 225)], 3: [(222, 225)], 5: [(222, 225)]}
        self.transition_dict[(222, 225)] = {1: [(22, 26)], 3: [(21, 27), (21, 25)],
                                            5: [(20, 28), (20, 25), (21, 23)]}  # extra cell for waiting one turn
        self.transition_dict[(22, 24)] = {1: [(22, 25)], 3: [(22, 25)], 5: [(22, 25)]}
        self.transition_dict[(22, 22)] = {1: [(21, 22)], 3: [(21, 24), (21, 20)],
                                          5: [(19, 26), (22, 19), (21, 18), (19, 20)]}
        self.transition_dict[(22, 20)] = {1: [(21, 20), (22, 19)], 3: [(21, 22), (19, 20), (21, 18)],
                                          5: [(17, 20), (21, 16), (21, 24)]}
        self.transition_dict[(22, 19)] = {1: [(21, 19), (22, 20)], 3: [(21, 21), (20, 20), (21, 17)],
                                          5: [(18, 20), (21, 15), (20, 16), (21, 23)]}
        self.transition_dict[(22, 18)] = {1: [(22, 17)], 3: [(22, 15)],
                                          5: [(21, 16), (21, 14)]}
        self.transition_dict[(22, 17)] = {1: [(22, 16)], 3: [(21, 15)],
                                          5: [(22, 14), (21, 17), (20, 16)], PAY: 120}  # BUY GLASSES
        self.transition_dict[(22, 16)] = {1: [(22, 15)], 3: [(21, 14), (21, 16)],
                                          5: [(21, 18), (19, 16)], PAY: 95}  # BUY HAT
        self.transition_dict[(22, 15)] = {1: [(21, 15)], 3: [(22, 14), (21, 17), (20, 16)],
                                          5: [(21, 19), (18, 16)]}
        self.transition_dict[(22, 14)] = {1: [(21, 14)], 3: [(21, 16)],
                                          5: [(21, 18), (19, 16)]}

    def init_row21(self):
        pass

    def init_row20(self):
        pass
    def init_row19(self):
        pass

    def init_row18(self):
        pass

    def init_row17(self):
        pass

    def init_row16(self):
        pass

    def init_row15(self):
        pass

    def init_row14(self):
        pass

    def init_row13(self):
        pass

    def init_row12(self):
        pass

    def init_row11(self):
        self.transition_dict[(11, 30)] = {1: [(10, 30), (11, 30)], 3: [(8, 30), (12, 28)],
                                          5: [(6, 30), (10, 28), (12, 26)], JUMP: []}

    def init_row10(self):
        self.transition_dict[(10, 30)] = {1: [(11, 30), (9, 30)], 3: [(7, 30), (12, 29)],
                                          5: [(5, 30), (11, 28), (12, 27)], JUMP: []}

    def init_row9(self):
        self.transition_dict[(9, 30)] = {1: [(10, 30), (11, 30)], 3: [(12, 30), (6, 30)], 5: [(5, 29), (12, 28)],
                                         JUMP: []}

    def init_row8(self):
        self.transition_dict[(8, 30)] = {1: [(9, 30), (7, 30)], 3: [(12, 30), (6, 30)], 5: [(5, 29), (12, 28)],
                                         JUMP: []}

    def init_row7(self):
        pass

    def init_row6(self):
        pass

    def init_row5(self):
        pass

    def init_row4(self):
        pass

    def init_row3(self):
        pass

    def init_row2(self):
        pass

    def init_row1(self):
        pass

    def init_row0(self):
        pass
