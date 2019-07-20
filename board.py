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
        self.transition_dict[(11,29)] = {1:[(10,29), (12,29)], 3:[(13,28), (12,27)], 5:[(6,29), (15,28), (12,25)], JUMP: []}
        self.transition_dict[(11,26)] = {1:[(10,26), (12,26)], 3:[(12,28), (8,26), (12,24), (13,25)], 5:[(6,26), (7,25), (12,30), (11,29), (14,28), (14,24), (15,25), (12,22)], JUMP: []}
        self.transition_dict[(11,22)] = {1:[(10,23), (12,24)], 3:[(8,22), (12,23), (12,20), (13,21)], 5:[(7,23), (7,21), (12,26), (13,25), (13,19), (12,18), (15,21)], JUMP: []}
        self.transition_dict[(11,21)] = {1:[(11,20)], 3:[(12,19)], 5:[(12,21), (11,18), (14,19)], JUMP: []}
        self.transition_dict[(11,20)] = {1:[(11,19)], 3:[(12,20), (12,18), (13,19)], 5:[(15,19), (12,22), (13,21), (10,18), (11,17)], JUMP: []}
        self.transition_dict[(11,19)] = {1:[(12,19)], 3:[(12,21), (14,19), (11,18)], 5:[(14,21), (12,23), (11,22), (15,18), (10,17), (11,16), (9,18)], JUMP: []}
        self.transition_dict[(11,18)] = {1:[(12,18), (10,18), (11,17)], 3:[(12,20),(13,19),(10,16),(12,16),(8,18),(9,17)],5:[(15,19),(13,21),(12,22),(7,19),(7,17),(12,15),(12,16),(10,16),(9,17)], JUMP: []}
        self.transition_dict[(11,17)] = {1:[(11,18), (11,16), (10,17)], 3:[(12,19),(12,15),(10,17),(9,18),(8,17)], 5:[(14,19),(12,21),(7,18),(7,16),(8,17)], JUMP: []}
        self.transition_dict[(11,16)] = {1:[(12,18), (10,16), (11,17)], 3:[(12,14),(12,18),(11,18),(10,18),(9,17)], 5:[(14,14),(12,12),(11,13),(13,19),(12,21),(7,17),(8,18),(9,17)], JUMP: []}
        self.transition_dict[(11,13)] = {1:[(12,13), (10,13)], 3:[(12,15),(12,11)], 5:[(11,16),(15,14),(11,10),(12,9)], JUMP: []}
        self.transition_dict[(11,10)] = {1:[(12,10), (11,9), (10,10)], 3:[(8,10),(9,9),(12,12),(12,8), (14,10),(13,9)], 5:[(7,11),(7,9),(12,14),(11,13),(12,6),(15,9),(14,8),(13,9)], JUMP: []}
        self.transition_dict[(11,9)] = {1:[(11,10), (12,9), (10,9)], 3:[(8,9),(9,14),(12,11),(12,7), (9,10)], 5:[(6,9),(7,10),(7,8),(8,11),(16,9),(15,8),(12,13),(12,5)], JUMP: []}
        self.transition_dict[(11,8)] = {1:[], 3:[], 5:[], JUMP: []}
        self.transition_dict[(11,7)] = {1:[], 3:[], 5:[], JUMP: []}
        self.transition_dict[(11,6)] = {1:[], 3:[], 5:[], JUMP: []}
        self.transition_dict[(11,5)] = {1:[], 3:[], 5:[], JUMP: []}
        self.transition_dict[(11,1)] = {1:[], 3:[], 5:[], JUMP: []}



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
