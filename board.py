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
        correction = {
            (11, 30): {1: [(10, 30), (11, 30)], 3: [(8, 30), (12, 28)], 5: [(6, 30), (10, 28), (12, 26)], 'jump': []},
            (11, 28): {1: [(10, 28), (12, 28)], 3: [(13, 27), (12, 26)], 5: [(6, 28), (15, 27), (12, 24)], 'jump': []},
            (11, 25): {1: [(10, 25), (12, 25)], 3: [(12, 27), (8, 25), (12, 23), (13, 24)],
                       5: [(6, 25), (7, 24), (12, 29), (11, 28), (14, 27), (14, 23), (15, 24), (12, 21)], 'jump': []},
            (11, 21): {1: [(10, 22), (12, 23)], 3: [(8, 21), (12, 22), (12, 19), (13, 20)],
                       5: [(7, 22), (7, 20), (12, 25), (13, 24), (13, 18), (12, 17), (15, 20)], 'jump': []},
            (11, 20): {1: [(11, 19)], 3: [(12, 18)], 5: [(12, 20), (11, 17), (14, 18)], 'jump': []},
            (11, 19): {1: [(11, 18)], 3: [(12, 19), (12, 17), (13, 18)],
                       5: [(15, 18), (12, 21), (13, 20), (10, 17), (11, 16)], 'jump': []},
            (11, 18): {1: [(12, 18)], 3: [(12, 20), (14, 18), (11, 17)],
                       5: [(14, 20), (12, 22), (11, 21), (15, 17), (10, 16), (11, 15), (9, 17)], 'jump': []},
            (11, 17): {1: [(12, 17), (10, 17), (11, 16)], 3: [(12, 19), (13, 18), (10, 15), (12, 15), (8, 17), (9, 16)],
                       5: [(15, 18), (13, 20), (12, 21), (7, 18), (7, 16), (12, 14), (12, 15), (10, 15), (9, 16)],
                       'jump': []},
            (11, 16): {1: [(11, 17), (11, 15), (10, 16)], 3: [(12, 18), (12, 14), (10, 16), (9, 17), (8, 16)],
                       5: [(14, 18), (12, 20), (7, 17), (7, 15), (8, 16)], 'jump': []},
            (11, 15): {1: [(12, 17), (10, 15), (11, 16)], 3: [(12, 13), (12, 17), (11, 17), (10, 17), (9, 16)],
                       5: [(14, 13), (12, 11), (11, 12), (13, 18), (12, 20), (7, 16), (8, 17), (9, 16)], 'jump': []},
            (11, 12): {1: [(12, 12), (10, 12)], 3: [(12, 14), (12, 10)], 5: [(11, 15), (15, 13), (11, 9), (12, 8)],
                       'jump': []},
            (11, 9): {1: [(12, 9), (11, 8), (10, 9)], 3: [(8, 9), (9, 8), (12, 11), (12, 7), (14, 9), (13, 8)],
                      5: [(7, 10), (7, 8), (12, 13), (11, 12), (12, 5), (15, 8), (14, 7), (13, 8)], 'jump': []},
            (11, 8): {1: [(11, 9), (12, 8), (10, 8)], 3: [(8, 8), (9, 13), (12, 10), (12, 6), (9, 9)],
                      5: [(6, 8), (7, 9), (7, 7), (8, 10), (16, 8), (15, 7), (12, 12), (12, 4)], 'jump': []}}

        self.transition_dict.update(correction)
        self.transition_dict[(11, 4)] = {1: [(12,4),(10,4)], 3: [(12,6), (14,4), (12,2),(8,4),(10,2)], 5: [(6,4),(7,5),(7,3),(10,0),(12,0),(12,8),(13,7),(16,4)], JUMP: []}
        self.transition_dict[(11, 0)] = {1: [(12,0),(10,0)], 3: [(14,0),(12,2),(10,2)], 5: [(10,4),(12,4),(16,0)], JUMP: []}

    def init_row10(self):
        self.transition_dict[(10, 30)] = {1: [(11, 30), (9, 30)], 3: [(7, 30), (12, 29)],
                                          5: [(5, 30), (11, 28), (12, 27)], JUMP: []}
        self.transition_dict[(10, 28)] = {1: [(11,28),(9,28)], 3:[(7,28), (12,29),(12,27)], 5:[(5,28),(6,27),(11,30),(12,25),(14,27)], JUMP:[]}
        self.transition_dict[(10, 25)] = {1: [(11,25),(9,25)], 3:[(7,25), (12,26),(12,24)], 5:[(5,25),(7,23),(6,26),(14,24),(12,22)], JUMP:[]}
        self.transition_dict[(10, 21)] = {1: [(11,21),(9,21)], 3:[(12,20), (12,22),(8,20),(7,21)], 5:[(7,23),(7,19),(14,20),(12,18),(12,24)], JUMP:[]}



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
