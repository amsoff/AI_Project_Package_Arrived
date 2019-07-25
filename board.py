import numpy as np
from enum import Enum
from Certificates import Certificate

JUMP = 'jump'
PAY = 'pay'
GET = 'get'
WAIT = 'wait'
HAS = 'has'
ORANGE = 150
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
        self.transition_dict[(22, 29)] = {1: [(22, 28)], 3: [(22, 28)], 5: [(22, 28)], JUMP: [(21, 28)]}
        self.transition_dict[(22, 28)] = {1: [(21, 28)], 3: [(21, 28)], 5: [(21, 28)], JUMP: [(20, 27)]}
        self.transition_dict[(22, 27)] = {1: [(22, 26), (21, 27)], 3: [(21, 25), (19, 27)],
                                          5: [(21, 23), (20, 24), (17, 27)]}
        self.transition_dict[(22, 26)] = {1: [(21, 26)], 3: [(21, 24), (20, 27)], 5: [(18, 27), (19, 24), (21, 21)]}
        self.transition_dict[(22, 25)] = {1: [(21, 25)], 3: [(21, 27), (20, 24), (21, 23), (22, 26)],
                                          5: [(19, 27), (19, 24), (21, 21)]}
        self.transition_dict[(22, 24)] = {1: [(222, 224)], 3: [(222, 224)], 5: [(222, 224)]}
        self.transition_dict[(222, 224)] = {1: [(22, 25)], 3: [(21, 26), (21, 24)], 5: [(20, 27), (20, 24), (21, 22)]}
        # extra cell for waiting one turn
        self.transition_dict[(22, 23)] = {1: [(22, 24)], 3: [(22, 24)], 5: [(22, 24)]}
        self.transition_dict[(22, 21)] = {1: [(21, 21)], 3: [(21, 23), (21, 19), (20, 20)],
                                          5: [(19, 25), (22, 18), (21, 17), (19, 19), (20, 22)]}
        self.transition_dict[(22, 19)] = {1: [(21, 19), (22, 18)], 3: [(21, 21), (19, 19), (21, 17), (20, 20)],
                                          5: [(17, 19), (21, 15), (21, 23), (20, 22), (22, 16)]}
        self.transition_dict[(22, 18)] = {1: [(21, 18), (22, 19)], 3: [(21, 20), (20, 19), (21, 16), (22, 17)],
                                          5: [(18, 19), (21, 14), (20, 15), (21, 22), (20, 21), (22, 15)]}
        self.transition_dict[(22, 17)] = {1: [(22, 16)], 3: [(22, 14)], 5: [(21, 15), (21, 13)]}
        self.transition_dict[(22, 16)] = {1: [(22, 15)], 3: [(21, 14)], 5: [(22, 13), (21, 16), (20, 15)], PAY: 120}
        # BUY GLASSES
        self.transition_dict[(22, 15)] = {1: [(22, 14)], 3: [(21, 13), (21, 15)], 5: [(21, 17), (19, 15)],
                                          PAY: 95}  # BUY HAT
        self.transition_dict[(22, 14)] = {1: [(21, 14)], 3: [(22, 13), (21, 16), (20, 15)], 5: [(21, 18), (18, 15)]}
        self.transition_dict[(22, 13)] = {1: [(21, 13)], 3: [(21, 15)], 5: [(21, 17), (19, 15)]}

    def init_row21(self):
        self.transition_dict[(21, 30)] = {1: [(22, 29)], 3: [(22, 29)], 5: [(22, 29)]}
        self.transition_dict[(21, 29)] = {1: [], 3: [], 5: []}
        self.transition_dict[(21, 28)] = {}  # END
        self.transition_dict[(21, 27)] = {1: [(21, 26), (20, 27)], 3: [(21, 24), (18, 27)],
                                          5: [(21, 22), (19, 24), (16, 27)]}
        self.transition_dict[(21, 26)] = {1: [(21, 27), (22, 26), (21, 25)], 3: [(20, 24), (21, 23), (19, 27)],
                                          5: [(21, 21), (18, 24), (17, 27)]}
        self.transition_dict[(21, 25)] = {1: [(21, 24), (21, 26)], 3: [(19, 24), (21, 22), (20, 27)],
                                          5: [(21, 20), (17, 24), (18, 27)]}
        self.transition_dict[(21, 24)] = {1: [(21, 25), (21, 23), (20, 24)],
                                          3: [(22, 26), (18, 24), (21, 21), (21, 27)],
                                          5: [(21, 19), (16, 24), (19, 27), (17, 23), (17, 25),
                                              (20, 20)]}  # get surprise

        self.transition_dict[(21, 23)] = {1: [(22, 23), (21, 24), (21, 22)],
                                          3: [(22, 24), (21, 26), (19, 24), (22, 21), (21, 20)],
                                          5: [(21, 18), (22, 19), (20, 19), (17, 24), (20, 27), (20, 21)]}
        self.transition_dict[(21, 22)] = {1: [(21, 23), (21, 21)], 3: [(21, 25), (20, 24), (21, 19), (20, 20)],
                                          5: [(21, 17), (19, 19), (22, 18), (21, 27), (18, 24), (20, 22)]}
        self.transition_dict[(21, 21)] = {1: [(22, 21), (21, 22), (21, 20)],
                                          3: [(20, 21), (20, 19), (21, 18), (22, 19), (21, 24)],
                                          5: [(21, 16), (22, 17), (19, 18), (21, 26), (19, 24), (20, 22)]}
        self.transition_dict[(21, 20)] = {1: [(20, 20), (21, 21), (21, 19)],
                                          3: [(20, 22), (21, 17), (22, 18), (21, 23), (19, 19)],
                                          5: [(21, 15), (22, 16), (18, 18), (21, 25), (20, 24), (20, 22)]}

        self.transition_dict[(21, 19)] = {1: [(22, 19), (21, 20), (21, 18), (20, 19)],
                                          3: [(20, 21), (22, 17), (21, 22), (18, 19), (21, 16)],
                                          5: [(20, 22), (22, 15), (21, 14), (21, 24), (17, 20), (17, 18), (20, 15)]}
        self.transition_dict[(21, 18)] = {1: [(21, 19), (22, 18), (21, 17)],
                                          3: [(22, 16), (21, 15), (19, 19), (21, 21), (20, 20)],
                                          5: [(22, 14), (20, 22), (21, 13), (21, 23), (17, 19), (19, 15)]}
        self.transition_dict[(21, 17)] = {1: [(21, 18), (22, 17), (21, 16)],
                                          3: [(21, 14), (20, 15), (22, 15), (21, 20), (20, 19), (22, 19)],
                                          5: [(20, 13), (21, 14), (18, 15), (17, 19), (22, 21), (21, 22), (22, 13),
                                              (19, 15)]}
        self.transition_dict[(21, 16)] = {1: [(21, 17), (21, 15)],
                                          3: [(21, 13), (19, 15), (22, 16), (22, 18), (21, 19)],
                                          5: [(19, 13), (22, 14), (17, 15), (21, 21), (20, 20), (19, 19)]}
        self.transition_dict[(21, 15)] = {1: [(21, 16), (21, 14), (20, 15)],
                                          3: [(22, 13), (20, 13), (18, 15), (22, 17), (21, 18)],
                                          5: [(17, 14), (16, 15), (18, 13), (22, 15), (22, 19), (21, 20), (20, 19)]}
        self.transition_dict[(21, 14)] = {1: [(21, 13), (21, 15)],
                                          3: [(19, 13), (19, 15), (21, 17)],
                                          5: [(17, 13), (18, 14), (17, 15), (22, 18), (22, 16), (21, 19)]}
        self.transition_dict[(21, 13)] = {1: [(22, 13), (21, 14), (20, 13)],
                                          3: [(18, 13), (20, 15), (21, 16)],
                                          5: [(17, 14), (17, 12), (16, 13), (18, 15), (22, 17), (21, 18)]}

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
        self.transition_dict[(11, 30)] = {1: [(10, 30), (11, 30)], 3: [(8, 30), (12, 28)], 5: [(6, 30), (10, 28), (12, 26)]}
        self.transition_dict[(11, 28)] = {1: [(10, 28), (12, 28)], 3: [(13, 27), (12, 26)], 5: [(6, 28), (15, 27), (12, 24)]}
        self.transition_dict[(11, 25)] = {1: [(10, 25), (12, 25)], 3: [(12, 27), (8, 25), (12, 23), (13, 24)],
                                          5: [(6, 25), (7, 24), (12, 29), (11, 28), (14, 27), (14, 23), (15, 24), (12, 21)]}
        self.transition_dict[(11, 21)] = {1: [(10, 22), (12, 23)], 3: [(8, 21), (12, 22), (12, 19), (13, 20)],
                                          5: [(7, 22), (7, 20), (12, 25), (13, 24), (13, 18), (12, 17), (15, 20)]}
        self.transition_dict[(11, 20)] = {1: [(11, 19)], 3: [(12, 18)], 5: [(12, 20), (11, 17), (14, 18)], PAY: 200}
        self.transition_dict[(11, 19)] = {1: [(4, 29)], 3: [(4, 29)],5: [(4, 29)]}
        self.transition_dict[(11, 18)] = {1: [(12, 18)], 3: [(12, 20), (14, 18), (11, 17)],
                                          5: [(14, 20), (12, 22), (11, 21), (15, 17), (10, 16), (11, 15), (9, 17)]}
        self.transition_dict[(11, 17)] = {1: [(12, 17), (10, 17), (11, 16)], 3: [(12, 19), (13, 18), (10, 15), (12, 15), (8, 17), (9, 16)],
                                          5: [(15, 18), (13, 20), (12, 21), (7, 18), (7, 16), (12, 14), (12, 15), (10, 15), (9, 16)]}
        self.transition_dict[(11, 16)] = {1: [(11, 17), (11, 15), (10, 16)], 3: [(12, 18), (12, 14), (10, 16), (9, 17), (8, 16)], 5: [(14, 18), (12, 20), (7, 17), (7, 15), (8, 16)]}
        self.transition_dict[(11, 15)] = {1: [(12, 17), (10, 15), (11, 16)], 3: [(12, 13), (12, 17), (11, 17), (10, 17), (9, 16)],
                                          5: [(14, 13), (12, 11), (11, 12), (13, 18), (12, 20), (7, 16), (8, 17), (9, 16)]}
        self.transition_dict[(11, 12)] = {1: [(12, 12), (10, 12)], 3: [(12, 14), (12, 10)], 5: [(11, 15), (15, 13), (11, 9), (12, 8)]}
        self.transition_dict[(11, 9)] = {1: [(12, 9),(10,9)], 3: [(8, 9),(9,8),(12,11),(13,8),(12,7)], 5: [(14,9),(12, 13),(11,12),(7,11),(7,8),(14,7),(12,5)]}
        self.transition_dict[(11, 8)] = {1: [(11, 9), (12, 8), (10, 8)], 3: [(8, 8), (9, 13), (12, 10), (12, 6), (9, 9)],
                                         5: [(6, 8), (7, 9), (7, 7), (8, 10), (16, 8), (15, 7), (12, 12), (12, 4)]}
        self.transition_dict[(11, 4)] = {1: [(12,4),(10,4)], 3: [(12,6), (14,4), (12,2),(8,4),(10,2)], 5: [(6,4),(7,5),(7,3),(10,0),(12,0),(12,8),(13,7),(16,4)]}
        self.transition_dict[(11, 0)] = {1: [(12,0),(10,0)], 3: [(14,0),(12,2),(10,2)], 5: [(10,4),(12,4),(16,0)]}

    def init_row10(self):
        self.transition_dict[(10, 30)] = {1: [(11, 30), (9, 30)], 3: [(7, 30), (12, 29)],
                                          5: [(5, 30), (11, 28), (12, 27)]}
        self.transition_dict[(10, 28)] = {1: [(11,28),(9,28)], 3:[(7,28), (12,29),(12,27)], 5:[(5,28),(6,27),(11,30),(12,25),(14,27)]}
        self.transition_dict[(10, 25)] = {1: [(11,25),(9,25)], 3:[(7,25), (12,26),(12,24)], 5:[(5,25),(7,23),(6,26),(14,24),(12,22)]}
        self.transition_dict[(10, 21)] = {1: [(11,21),(9,21)], 3:[(12,20), (12,22),(8,20),(7,21)], 5:[(7,23),(7,19),(14,20),(12,18),(12,24)]}
        self.transition_dict[(10, 20)] = {1: [(11,20)], 3:[(11,18)], 5:[(12,19),(12,17),(13,18)],  PAY: 150}
        self.transition_dict[(10, 17)] = {1: [(10,17),(10,16),(9,17)], 3:[(12,18),(7,17),(11,15),(8,16)], 5:[(12,20),(14,18),(12,14),(7,19),(7,15)]}
        self.transition_dict[(10, 16)] = {1: [(10,17),(9,16),(11,16),(10,15)], 3:[(12,15),(8,17),(7,16),(12,17)], 5:[(7,18),(7,14),(7,16),(12,13),(12,19),(13,18)]}
        self.transition_dict[(10, 15)] = {1: [(11,15),(10,16)], 3:[(12,14),(11,17),(8,16),(9,17)], 5:[(13,13),(12,12),(12,19),(13,18),(7,18),(6,16),(7,15)]}
        self.transition_dict[(10, 12)] = {1: [(9,12),(11,12)], 3:[(12,13),(12,11)], 5:[(12,9),(13,14),(12,15)]}
        self.transition_dict[(10, 9)] = {1: [(10,8),(9,9),(11,9)], 3:[(12,10),(12,8),(7,9),(8,8)], 5:[(7,11),(7,7),(6,8),(12,12),(12,5),(14,8),(13,7)]}
        self.transition_dict[(10, 8)] = {1: [(10,9),(11,8),(9,8)], 3:[(8,9),(13,8),(12,7),(7,8),(12,9)], 5:[(5,8),(7,6),(7,10),(15,8),(12,11),(12,5),(14,7)]}
        self.transition_dict[(10, 4)] = {1: [(11,4),(10,3),(9,4)], 3:[(7,4),(10,1),(12,5),(12,3)], 5:[(7,6),(7,2),(11,0),(12,7),(12,1)]}
        self.transition_dict[(10, 3)] = {1: [(10,4),(10,2)], 3:[(8,4),(12,4),(10,0)], 5:[(14,4),(12,0),(12,2),(12,6),(7,5),(6,4),(7,3)]}
        self.transition_dict[(10, 2)] = {1: [(10,3),(10,1)], 3:[(11,0),(9,4),(11,4)], 5:[(12,1),(13,0),(8,3),(7,4),(12,5),(13,4),(12,3)]}
        self.transition_dict[(10, 1)] = {1: [(10,0),(10,2)], 3:[(12,0),(10,4)], 5:[(12,2),(14,0),(8,4),(12,4)]}
        self.transition_dict[(10, 0)] = {1: [(10,1),(11,0)], 3:[(12,1),(13,0),(10,3)], 5:[(15,0),(12,3),(9,4),(11,4)]}

    def init_row9(self):
        self.transition_dict[(9, 30)] = {1: [(10, 30), (11, 30)], 3: [(12, 30), (6, 30)], 5: [(5, 29), (12, 28)],
                                         JUMP: []}
        self.transition_dict[(9, 28)] = {1: [(10,28),(8,28)], 3:[(12,28),(6,28)], 5:[(12,29),(12,27),(6,27),(5,28)]}
        self.transition_dict[(9, 27)] = {1: [(9,28)], 3:[(11,28),(7,28)], 5:[(12,29),(12,27),(6,27),(5,28)]}
        self.transition_dict[(9, 26)] = {1: [(9,27)], 3:[(7, 26)], 5:[(6,28),(12,28)]}
        self.transition_dict[(7, 26)] = {1: [(9,27)], 3:[(10,28),(8,28)], 5:[(6,28),(12,28)],  GET: 1500}
        self.transition_dict[(9, 25)] = {1: [(9,26),(10,25),(8,25)], 3:[(6,25),(12,25),(9,28)], 5:[(7,22),(6,27),(9,28),(12,23),(12,27),(4,25)]}
        self.transition_dict[(9, 21)] = {1: [(10,21),(8,21)], 3:[(7,22),(7,20),(12,21)], 5:[(13,20),(12,19),(12,23),(7,24),(18,7)]}
        self.transition_dict[(9, 21)] = {1: [(10,21),(8,21)], 3:[(7,22),(7,20),(12,21)], 5:[(13,20),(12,19),(12,23),(7,24),(18,7)]}
        self.transition_dict[(9, 20)] = {1: [(9,19)], 3:[(9,19)], 5:[(9,19)]}
        self.transition_dict[(9, 19)] = {1: [(9,18)], 3:[(9,18)], 5:[(9,18)]}
        self.transition_dict[(9, 18)] = {1: [(10,20)], 3:[(11,19)], 5:[(12,18)]}
        self.transition_dict[(9, 17)] = {1: [(10,17)], 3:[(8,17),(10,17),(9,16)], 5:[(7,20),(5,18),(7,14),(12,19),(12,15)]}
        self.transition_dict[(9, 16)] = {1: [(10,16),(8,16),(9,17)], 3:[(11,15),(11,17),(7,17),(7,15)], 5:[(12,14),(12,18),(7,13),(7,19),(6,18)]}
        self.transition_dict[(9, 12)] = {1: [(10,12)], 3:[(12,12)], 5:[(12,10),(12,14),(13,13)]}
        self.transition_dict[(9, 9)] = {1: [(10,9),(9,8),(8,9)], 3:[(12,9),(7,8),(7,10),(11,8)], 5:[(7,12),(6,11),(5,8),(7,6),(12,11),(12,7),(13,8)]}
        self.transition_dict[(9, 8)] = {1: [(10,8),(8,8),(9,9)], 3:[(12,8),(11,9),(6,8),(7,7),(7,9)], 5:[(4,8),(7,11),(7,5),(14,8),(13,7),(12,10),(11,9),(12,6)]}
        self.transition_dict[(9, 7)] = {1: [(9,6)], 3:[(9,6)], 5:[(9,6)]}
        self.transition_dict[(9, 6)] = {1: [(9,5)], 3:[(9,5)], 5:[(9,5)]}
        self.transition_dict[(9, 5)] = {1: [(9,4)], 3:[(11,4),(7,4),(10,3)], 5:[(5,4),(7,6),(7,2),(10,3),(11,4)], HAS:Certificate.RABIES}
        self.transition_dict[(9, 4)] = {1: [(8,4),(10,4)], 3:[(6,4),(7,5),(7,3),(10,2),(12,4)], 5:[(7,7),(7,1),(4,4),(10,0),(12,6),(12,2)]}
        self.transition_dict[(9, 3)] = {1: [(10,3)], 3:[(10,1),(11,4),(7,4)], 5:[(11,0),(12,5),(13,4),(12,3),(7,6),(7,2),(5,4)]}

    def init_row8(self):
        self.transition_dict[(8, 30)] = {1: [(9, 30), (7, 30)], 3: [(12, 30), (6, 30)], 5: [(5, 29), (12, 28)],
                                         JUMP: []}
        self.transition_dict[(8, 28)] = {1: [(9,28),(7,28)], 3:[(5,28),(11,28),(6,27)], 5:[(6,25),(5,30),(3,28),(12,29),(12,27)]}
        self.transition_dict[(8, 25)] = {1: [(9,25),(7,25)], 3:[(11,25),(7,24),(5,25),(6,26)], 5:[(6,28),(7,21),(3,25),(12,27),(12,24)]}
        self.transition_dict[(8, 21)] = {1: [(8,20)], 3:[(8,20)], 5:[(8,20)]}
        self.transition_dict[(8, 20)] = {1: [(9,20)], 3:[(11,20)], 5:[(11,18)]}
        self.transition_dict[(8, 17)] = {1: [(9,17),(8,16),(7,17)], 3:[(11,17),(7,15),(6,18),(6,16)], 5:[(12,18),(7,13),(6,20),(7,21),(11,15)]}
        self.transition_dict[(8, 16)] = {1: [(8,17),(7,16),(9,16)], 3:[(11,16),(10,17),(7,14),(7,18),(5,16)], 5:[(12,15),(12,17),(7,20),(5,18),(8,13)]}
        self.transition_dict[(8, 13)] = {1: [(7,13)], 3:[(7,11),(7,15)], 5:[(8,16),(6,16),(5,11),(8,10),(7,9)]}
        self.transition_dict[(8, 10)] = {1: [(7,10),(8,9)], 3:[(8,7),(7,8),(9,8),(10,9),(6,11)], 5:[(7,14),(8,13),(4,11),(5,8),(7,6),(11,8),(12,9)]}
        self.transition_dict[(8, 9)] = {1: [(8,10),(8,8),(9,9),(7,9)], 3:[(7,11),(6,8),(7,7),(11,9),(10,8)], 5:[(5,11),(7,13),(8,6),(7,5),(12,10),(12,8)]}
        self.transition_dict[(8, 8)] = {1: [(8,9),(9,8),(7,8),(7,8)], 3:[(9,7),(7,10),(11,8),(7,6)], 5:[(9,5),(12,7),(7,4),(6,11),(7,12),(12,9)]}
        self.transition_dict[(8, 7)] = {1: [(8,6)], 3:[(9,6)], 5:[(9,5)]}
        self.transition_dict[(8, 6)] = {1: [(9,7)], 3:[(9,5)], 5:[(10,4),(8,4)]}
        self.transition_dict[(8, 4)] = {1: [(8,3),(9,4),(7,4)], 3:[(10,3),(5,4),(7,6),(7,2)], 5:[(10,4),(12,5),(12,3),(10,1),(3,4),(7,8)]}
        self.transition_dict[(8, 3)] = {1: [(8,2)], 3:[(10,4),(10,2)], 5:[(8,4),(12,4),(10,0)]}
        self.transition_dict[(8, 2)] = {1: [(9,3)], 3:[(10,4),(10,2)], 5:[(8,4),(12,4),(10,0)], GET: 1000}

    def init_row7(self):
        self.transition_dict[(7, 30)] = {1: [(6, 30),(8,30)], 3: [(10,30), (5,29)], 5: [(4,28), (6,28), (12, 30)]}
        self.transition_dict[(7, 28)] = {1: [(8, 28),(6,28)], 3: [(10,28), (5,29),(4,28),(6,26)], 5: [(6,30), (7,25), (5, 25),(3,28),(12,28)]}
        self.transition_dict[(7, 25)] = {1: [(8, 25),(6,25), (7,24)], 3: [(7,22), (10,25),(4,25),(6,27)], 5: [(8,21), (7,20), (7, 28),(5,28),(12,25)]}
        self.transition_dict[(7, 24)] = {1: [(7, 25),(7,23)], 3: [(7,21),(6,22), (9,25),(5,25),(6,26)], 5: [(8,20), (9,21), (7,19) ,(6,20),(11,25),(6,28),(3,25),(6,24)]}
        self.transition_dict[(7, 23)] = {1: [(7, 24),(7,22)], 3: [(8,21), (7,20),(8,25),(6,25)], 5: [(10,25), (6,27), (4,25) ,(10,21),(8,20),(7,18),(5,20)]}
        self.transition_dict[(7, 22)] = {1: [(7, 23),(7,21),(6,22)], 3: [(7,25), (8,20),(9,21),(7,19),(6,20),(6,24)], 5: [(9,25), (6,26), (5,25) ,(4,20),(6,18),(11,21),(5,20),(5,23)]}
        self.transition_dict[(7, 21)] = {1: [(7, 22),(7,20),(8,21)], 3: [(7,24), (10,21),(7,18),(5,20),(8,20)], 5: [(8,20), (8,25), (6,25) ,(12,21),(5,18),(3,20)]}
        self.transition_dict[(7, 20)] = {1: [(7, 21),(7,19),(6,20)], 3: [(6,18), (4,20),(8,20),(7,23),(7,17),(6,22)], 5: [(7,25), (2,20), (4,18) ,(8,20),(11,21),(6,16),(17,15),(9,17),(6,24)]}
        self.transition_dict[(7, 19)] = {1: [(7, 20),(7,18)], 3: [(5,18), (5,20),(7,22),(8,21),(7,16)], 5: [(7,24), (8,20), (10,21) ,(3,20),(3,18),(10,17),(9,16),(5,16),(7,14)]}
        self.transition_dict[(7, 18)] = {1: [(7, 19),(7,17),(6,18)], 3: [(7,21), (6,20),(4,18),(7,15),(9,17),(8,16)], 5: [(8,20), (7,23), (4,20),(9,21),(3,17),(11,17),(10,16),(7,13),(5,16)]}
        self.transition_dict[(7, 17)] = {1: [(7, 18),(7,16),(8,17)], 3: [(7,20), (5,18),(5,16),(7,14),(10,17),(10,16)], 5: [(8,13), (8,12), (3,16),(7,22),(8,21),(5,20),(3,18),(3,16),(7,12)]}
        self.transition_dict[(7, 16)] = {1: [(7, 17),(7,15),(8,16),(6,16)], 3: [(7,19), (10,16),(7,13),(4,16),(6,18),(8,17)], 5: [(7,21), (3,17), (3,14),(7,11),(11,16),(11,15)]}
        self.transition_dict[(7, 15)] = {1: [(7, 16),(7,14)], 3: [(7,12), (8,13),(9,16),(8,17),(7,18),(5,16)], 5: [(10,17), (11,16), (7,20),(3,16),(7,10)]}
        self.transition_dict[(7, 14)] = {1: [(7, 15),(7,13)], 3: [(8,16), (6,16),(7,17),(7,11)], 5: [(10,16), (9,17), (7,19),(4,16),(7,9)]}
        self.transition_dict[(7, 13)] = {1: [(7, 14),(7,12),(8,13)], 3: [(7,16), (7,10)], 5: [(8,9), (7,18), (5,16),(4,11)]}
        self.transition_dict[(7, 12)] = {1: [(7, 13),(7,11)], 3: [(7,9), (8,10),(7,15)], 5: [(7,17), (8,16), (6,16),(7,7),(8,8),(6,8),(9,9)]}
        self.transition_dict[(7, 11)] = {1: [(7, 12),(7,10),(6,11)], 3: [(7,13), (4,11),(7,8),(8,9),(5,13)], 5: [(7,16), (2,11),(5,13),(3,10),(8,8),(7,6)]}
        self.transition_dict[(7, 10)] = {1: [(7, 11),(8,10),(7,9)], 3: [(7,13), (5,11),(7,7),(6,8),(9,9)], 5: [(7,15), (5,13),(3,11),(7,5),(8,8),(9,9),(10,8)]}
        self.transition_dict[(7, 9)] = {1: [(8,9),(7,10),(7,8)], 3: [(10,9), (8,7),(7,12),(7,6),(5,8)], 5: [(12,9), (9,6),(8,13),(7,14),(3,8)]}
        self.transition_dict[(7, 8)] = {1: [(7,9),(8,8),(6,8),(7,7)], 3: [(8,10), (7,11),(4,8),(7,5),(10,8)], 5: [(7,13), (11,9),(12,8),(9,5),(8,4),(7,3),(6,4),(3,9),(2,8),(3,7)]}
        self.transition_dict[(7, 7)] = {1: [(7,8),(7,6)], 3: [(8,7), (7,4),(7,10),(9,8),(5,8),(8,9)], 5: [(8,3), (7,2),(9,4),(5,4),(3,8),(7,12),(10,8),(10,9)]}
        self.transition_dict[(7, 6)] = {1: [(7,7),(7,5)], 3: [(8,8), (7,9),(6,8),(8,4),(7,3),(6,4)], 5: [(10,8), (7,11),(4,8),(10,4),(4,4),(7,1),(9,3)]}
        self.transition_dict[(7, 5)] = {1: [(7,6),(7,4)], 3: [(7,8), (7,2),(8,3),(9,4),(5,4)], 5: [(8,7), (6,8),(7,9),(8,8),(11,4),(3,4),(7,0)]}
        self.transition_dict[(7, 4)] = {1: [(7,5),(7,3),(6,4),(8,4)], 3: [(10,4), (7,1),(4,4),(7,7),(9,3)], 5: [(7,9), (2,4),(12,4),(10,2)]}
        self.transition_dict[(7, 3)] = {1: [(7,4),(7,2)], 3: [(9,4), (7,0),(7,6),(5,4)], 5: [(11,4), (10,3),(3,4)]}
        self.transition_dict[(7, 2)] = {1: [(7,1),(7,3)], 3: [(7,5), (6,4),(8,4)], 5: [(10,4), (4,4),(7,7),(9,3)]}
        self.transition_dict[(7, 1)] = {1: [(7,0),(7,2)], 3: [(7,4)], 5: [(9,4), (5,4),(7,6),(8,3)]}
        self.transition_dict[(7, 0)] = {1: [(7,1)], 3: [(7,3)], 5: [(8,3), (7,5),(6,4)]}

    def init_row6(self):
        self.transition_dict[(6, 30)] = {1: [(7, 30),(5,30)], 3: [(5, 28),(9,30)], 5: [(3, 28), (11, 30), (7, 28),(6,27)]}
        self.transition_dict[(6, 28)] = {1: [(7, 28),(5,28),(6,27)], 3: [(3, 28),(6,25),(5,30),(9,28)], 5: [(7, 30), (2,28), (11, 28),(8,25),(7,24),(4,25)]}
        self.transition_dict[(6, 27)] = {1: [(6, 28),(6,26)], 3: [(8, 28),(4,28),(5,29),(7,25),(5,25)], 5: [(9, 25), (10,28), (3, 25),(6,30),(4,28)]}
        self.transition_dict[(6, 26)] = {1: [(6, 27),(6,25)], 3: [(5, 28),(7,28),(7,24),(8,25),(4,25)], 5: [(9, 28), (5,30), (2, 25),(3,28),(7,22),(10,25)]}
        self.transition_dict[(6, 25)] = {1: [(6, 26),(5,25),(7,25)], 3: [(3, 25),(6,28),(9,25),(7,23)], 5: [(8, 28), (5,29), (4, 28),(1,25),(7,21),(11,25)]}
        self.transition_dict[(6, 24)] = {1: [(5, 24)], 3: [(5, 22)], 5: [(6, 24)], ORANGE: True}
        self.transition_dict[(6, 23)] = {1: [(6, 24)], 3: [(5, 23)], 5: [(6, 24)], PAY: 50, ORANGE: True}
        self.transition_dict[(6, 22)] = {1: [(6, 23)], 3: [(5, 24)], 5: [(6, 21)], WAIT: True}
        self.transition_dict[(6, 20)] = {1: [(5, 20),(7,20)], 3: [(7,22),(3,22),(7,18),(8,21)], 5: [(3, 18),(1,20),(5,18),(8,20),(10,21),(7,24)]}
        self.transition_dict[(6, 18)] = {1: [(7, 18),(5,18)], 3: [(7,20),(8,17),(7,16),(3,18)], 5: [(7, 22),(8,21),(5,20),(3,20),(3,16),(9,17),(7,14),(10,17),(9,16)]}
        self.transition_dict[(6, 17)] = {1: [(5, 17),(7,16)], 3: [(3,16),(7,18),(7,14),(9,16),(8,17)], 5: [(7, 22),(8,21),(5,20),(3,20),(3,16),(9,17),(7,14),(10,17),(9,16)]}
        self.transition_dict[(6, 14)] = {1: [(5, 14)], 3: [(3,14)], 5: [(3, 16),(3,12)]}
        self.transition_dict[(6, 13)] = {1: [(6, 14)], 3: [(4,14)], 5: [(3, 15),(3,13)]}
        self.transition_dict[(6, 11)] = {1: [(7, 11),(5,11)], 3: [(3,11),(5,13),(7,13),(7,9),(8,10)], 5: [(3, 13),(3,9),(1,11),(7,15),(8,8),(7,7),(9,9)]}
        self.transition_dict[(6, 8)] = {1: [(7, 8),(5,8)], 3: [(3,8),(7,10),(7,6),(9,8),(8,9)], 5: [(7, 12),(9,7),(1,8),(3,10),(3,6),(8,8),(7,4),(11,8)]}
        self.transition_dict[(6, 4)] = {1: [(7, 4),(5,4)], 3: [(4,4),(7,6),(7,2),(8,3),(9,4)], 5: [(8, 7),(7,8),(3,6),(1,4),(7,0),(11,4),(10,3)]}

    def init_row5(self):
        self.transition_dict[(5, 30)] = {1: [(6, 30),(5,29)], 3: [(4,28),(6,28),(8,30)], 5: [(10, 30),(2,28),(8,28),(6,26)]}
        self.transition_dict[(5, 29)] = {1: [(5, 30),(5,28)], 3: [(7,30),(7,28),(3,28),(6,27)], 5: [(9,30),(9,28),(6,25)]}
        self.transition_dict[(5, 28)] = {1: [(5, 29),(4,28),(6,28)], 3: [(6,30),(8,28),(6,26),(2,28)], 5: [(9,30),(9,28),(6,25)]}
        self.transition_dict[(5, 27)] = {1: [(5, 28)], 3: [(5,30),(7,28),(3,28),(6,27)], 5: [(7,30),(9,28),(6,25)]}
        self.transition_dict[(5, 25)] = {1: [(6, 25), (4,25)], 3: [(6,28),(2,25),(8,25),(7,24)], 5: [(5,28),(7,28),(10,25),(7,22),(0,25),(3,26)]}
        self.transition_dict[(5, 24)] = {1: [(5,23)], 3: [(5,24)], 5: [(5,24)], ORANGE: True}
        self.transition_dict[(5, 23)] = {1: [(5,22)], 3: [(5,23)], 5: [(5,23)], ORANGE: True}
        self.transition_dict[(5, 22)] = {1: [(5,21)], 3: [(6,20),(4,20)], 5: [(7,21),(7,19),(2,20),(3,19),(1,20)], HAS: Certificate.ID}
        self.transition_dict[(5, 21)] = {1: [(5,20)], 3: [(7,20),(3,20)], 5: [(7,18),(7,22),(8,21),(3,18),(1,20)]}
        self.transition_dict[(5, 20)] = {1: [(6,20),(4,20)], 3: [(7,21),(7,19),(2,20),(3,19)], 5: [(9,21),(7,23),(6,18),(4,18),(3,17),(0,20)]}
        self.transition_dict[(5, 18)] = {1: [(6,18),(4,18)], 3: [(7,19),(3,19),(3,17)], 5: [(6,20),(7,21),(6,18),(4,20),(4,16),(3,15),(2,20)]}
        self.transition_dict[(5, 17)] = {1: [(4,17)], 3: [(6,17)], 5: [(7,18),(3,20),(3,16)]}
        self.transition_dict[(6, 17)] = {1: [(4,17)], 3: [(5,18),(3,18)], 5: [(7,18),(3,20),(3,16)], GET: 1000}
        self.transition_dict[(5, 16)] = {1: [(4,16),(6,16),(5,17)], 3: [(3,17),(3,15),(7,16)], 5: [(6,18),(3,19),(3,18),(3,13),(7,19),(6,18),(7,13)]}
        self.transition_dict[(5, 15)] = {1: [(5,14)], 3: [(3,14)], 5: [(3,16),(3,12)]}
        self.transition_dict[(5, 14)] = {1: [(4,14)], 3: [(3,15),(3,13)], 5: [(3,17),(4,16),(3,11)]}
        self.transition_dict[(5, 13)] = {1: [(6,13)], 3: [(5,14)], 5: [(3,14)]}
        self.transition_dict[(5, 12)] = {1: [(5,13)], 3: [(5,13)], 5: [(5,13)]}
        self.transition_dict[(5, 11)] = {1: [(5,12),(4,11),(6,11)], 3: [(5,13),(3,12),(2,11),(3,10),(7,12),(7,10)], 5: [(5,13),(7,14),(3,14),(11,0),(3,8),(7,8),(8,9)]}
        self.transition_dict[(5, 8)] = {1: [(6,8),(4,8)], 3: [(4,6),(3,9),(3,7),(2,8),(8,8),(7,9),(7,7)], 5: [(3,11),(0,8),(4,5),(3,5),(7,5),(7,11),(8,6),(10,8)]}
        self.transition_dict[(5, 4)] = {1: [(5,6),(4,4)], 3: [(8,4),(7,5),(7,3),(2,4),(3,5)], 5: [(0,4),(3,7),(9,3),(7,1),(7,7),(10,4)]}

    def init_row4(self):
        self.transition_dict[(4, 30)] = {1: [(3,30)], 3: [(2,29)], 5: [(3,28)]}
        self.transition_dict[(4, 29)] = {1: [(4,30)], 3: [(3,29)], 5: [(2,28)]}
        self.transition_dict[(4, 28)] = {1: [(5,28),(4,29),(3,28)], 3: [(3,30),(5,30),(6,27),(7,28)], 5: [(2,29),(7,30),(9,28),(6,25)]}
        self.transition_dict[(4, 27)] = {1: [(5,27)], 3: [(6,28),(6,26)], 5: [(7,25),(5,25),(8,28),(5,29),(4,29)]}
        self.transition_dict[(4, 25)] = {1: [(5,25),(3,25)], 3: [(6,26),(7,25),(2,26),(1,25)], 5: [(0,26),(0,24),(6,28),(7,23),(9,25)], ORANGE: True}
        self.transition_dict[(4, 20)] = {1: [(5,20),(3,20)], 3: [(1,20),(3,18),(7,20)], 5: [(0,21),(3,16),(7,22),(8,21),(7,18),(5,18)]}
        self.transition_dict[(4, 18)] = {1: [(5,18),(3,18)], 3: [(7,18),(3,20),(3,16)], 5: [(1,20),(5,20),(5,16),(3,14)]}
        self.transition_dict[(4, 17)] = {1: [(4,18)], 3: [(6,18),(3,19),(3,17)], 5: [(7,19),(4,20),(2,20),(4,16),(3,15)]}
        self.transition_dict[(4, 16)] = {1: [(5,16),(3,16)], 3: [(3,18),(3,14),(7,16),(4,17)], 5: [(3,20),(5,18),(3,12),(7,18),(7,14),(9,16)]}
        self.transition_dict[(4, 14)] = {1: [(3,14)], 3: [(3,16),(3,12)], 5: [(4,11),(2,11),(3,10),(1,12),(5,16),(3,18)]}
        self.transition_dict[(4, 11)] = {1: [(4,10),(5,11),(3,11)], 3: [(1,11),(3,13),(3,9),(4,8),(5,13)], 5: [(3,15),(4,8),(2,8),(3,7),(7,13),(8,10),(7,9)]}
        self.transition_dict[(4, 10)] = {1: [(4,9)], 3: [(5,8),(4,7),(3,8)], 5: [(5,10)]}
        self.transition_dict[(5, 10)] = {1: [(4,9)], 3: [(5,8),(4,7),(3,8)], 5: [(4,5),(7,8),(3,10),(3,6),(1,8)], GET: 500}
        self.transition_dict[(4, 9)] = {1: [(4,8)], 3: [(6,8),(4,6),(3,7),(2,8),(3,9)], 5: [(4,5),(0,8),(3,11),(3,5),(7,9),(8,8),(7,7)]}
        self.transition_dict[(4, 8)] = {1: [(5,8),(3,8),(4,7)], 3: [(4,5),(1,8),(3,10),(7,8)], 5: [(4,5),(3,12),(4,11),(2,11),(3,4),(8,7),(8,9),(7,10),(7,6)]}
        self.transition_dict[(4, 7)] = {1: [(4,6)], 3: [(4,5)], 5: [(4,5)]}
        self.transition_dict[(4, 6)] = {1: [(4,5)], 3: [(4,5)], 5: [(4,5)]}
        self.transition_dict[(4, 5)] = {1: [(4,4)], 3: [(6,4),(2,4),(3,5)], 5: [(3,7),(7,5),(8,4),(7,3)], PAY: 50, HAS: Certificate.HAIRCUT}
        self.transition_dict[(4, 4)] = {1: [(5,4),(3,4)], 3: [(7,4),(1,4),(3,6)], 5: [(3,8),(7,2),(7,6),(8,3)]}


    def init_row3(self):
        self.transition_dict[(3, 30)] = {1: [(3,29)], 3: [(2,28)], 5: [(4,28)]}
        self.transition_dict[(3, 29)] = {1: [(2,29)], 3: [(3,28)], 5: [(5,28)]}
        self.transition_dict[(3, 28)] = {1: [(2,28),(4,28)], 3: [(5,29),(6,28)], 5: [(6,30),(7,28),(6,26)]}
        self.transition_dict[(3, 27)] = {1: [(4,27)], 3: [(6,27)], 5: [(6,25),(5,28),(7,28)]}
        self.transition_dict[(3, 26)] = {1: [(3,27)], 3: [(5,27)], 5: [(6,26),(6,28)]}
        self.transition_dict[(3, 25)] = {1: [(2,25),(4,25)], 3: [(0,25),(3,26),(6,25)], 5: [(0,27),(0,23),(6,27),(8,25),(7,24)], ORANGE: True}
        self.transition_dict[(3, 20)] = {1: [(2,20),(4,20),(3,19)], 3: [(6,20),(3,17),(0,20)], 5: [(0,22),(7,21),(6,18),(4,16),(3,15)]}
        self.transition_dict[(3, 19)] = {1: [(3,20),(3,18)], 3: [(1,20),(5,20),(3,16),(5,18)], 5: [(7,20),(7,18),(3,14),(5,16)]}
        self.transition_dict[(3, 18)] = {1: [(3,19),(4,18),(3,17)], 3: [(6,18),(4,20),(2,20),(4,16),(3,15)], 5: [(7,19),(6,20),(0,20),(5,17),(3,13),(6,16)]}
        self.transition_dict[(3, 17)] = {1: [(3,18),(3,16)], 3: [(3,20),(5,18),(5,16),(3,14)], 5: [(5,20),(7,18),(7,16),(1,20),(3,12)]}
        self.transition_dict[(3, 16)] = {1: [(3,17),(3,15),(4,16)], 3: [(3,18),(6,16),(3,13),(5,17)], 5: [(2,20),(4,20),(6,18),(7,17),(7,15),(3,11)]}
        self.transition_dict[(3, 15)] = {1: [(3,16),(3,14)], 3: [(5,16),(3,18),(3,12)], 5: [(4,11),(3,10),(2,11),(7,16),(5,18),(3,20)]}
        self.transition_dict[(3, 14)] = {1: [(3,15),(3,13)], 3: [(2,12),(3,11),(4,16),(3,17)], 5: [(5,17),(1,13),(3,19),(4,18),(5,11),(1,11),(3,9),(4,0)]}
        self.transition_dict[(3, 13)] = {1: [(3,14),(3,12)], 3: [(3,16),(1,12),(3,10),(2,11),(4,11)], 5: [(3,18),(5,16),(2,13),(5,12),(3,8),(0,11),(6,11)]}
        self.transition_dict[(3, 12)] = {1: [(3,13),(3,11)], 3: [(3,15),(1,13),(1,11),(5,11),(4,10),(3,9)], 5: [(5,13),(3,17),(4,8),(2,8),(3,7),(7,11)]}
        self.transition_dict[(3, 11)] = {1: [(3,12),(3,10),(2,11),(4,11)], 3: [(3,14),(0,11),(1,12),(6,11),(3,8)], 5: [(3,16),(2,13),(5,8),(5,13),(7,12),(7,10),(3,6)]}
        self.transition_dict[(3, 10)] = {1: [(3,11),(3,9)], 3: [(3,13),(1,11),(3,13),(4,8),(3,7),(2,8)], 5: [(5,13),(3,15),(6,8),(0,8),(3,5),(7,11)]}
        self.transition_dict[(3, 9)] = {1: [(3,8),(3,10)], 3: [(4,11),(3,12),(2,11),(5,8),(1,8),(3,6),(4,7)], 5: [(5,12),(0,11),(3,14),(0,8),(3,4),(7,8),(6,11)]}
        self.transition_dict[(3, 8)] = {1: [(3,9),(3,7),(4,8),(2,8)], 3: [(6,8),(3,11),(3,5),(0,8),(4,6)], 5: [(3,13),(1,11),(4,5),(4,4),(2,4),(7,9),(7,7),(5,11)]}
        self.transition_dict[(3, 7)] = {1: [(3,8),(3,6)], 3: [(4,7),(3,10),(1,8),(3,4)], 5: [(3,12),(4,5),(1,4),(5,4),(7,8),(4,11),(2,11),(0,9)]}
        self.transition_dict[(3, 6)] = {1: [(3,5),(3,7)], 3: [(4,8),(3,9),(2,4),(4,4),(2,8)], 5: [(6,4),(0,4),(0,8),(6,8),(3,11),(4,6)]}
        self.transition_dict[(3, 5)] = {1: [(3,6),(3,4)], 3: [(3,8),(5,4),(1,4)], 5: [(7,4),(1,8),(5,8),(4,7),(3,0)]}
        self.transition_dict[(3, 4)] = {1: [(3,5),(4,4),(2,4)], 3: [(3,7),(6,4),(0,4)], 5: [(3,9),(2,8),(4,8),(7,5),(8,4),(7,3)]}


    def init_row2(self):
        self.transition_dict[(2, 29)] = {1: [(2,28)], 3: [(4,28)], 5: [(5,29),(6,28)]}
        self.transition_dict[(2, 28)] = {1: [(3,28)], 3: [(5,28)], 5: [(5,30),(7,28),(6,27)]}
        self.transition_dict[(2, 26)] = {1: [(3,26)], 3: [(2,26)], 5: [(2,26)], ORANGE: [(3,26)]}
        self.transition_dict[(2, 25)] = {1: [(3,25),(1,25), (2,26)], 3: [(5,25),(0,26),(0,24)], 5: [(0,22),(6,26),(7,25)], ORANGE: [(3,26)]}
        self.transition_dict[(2, 20)] = {1: [(1,20),(3,20)], 3: [(0,21),(3,18),(5,20)], 5: [(0,23),(7,20),(5,18),(3,16)]}
        self.transition_dict[(2, 15)] = {1: [(3,15)], 3: [(3,13),(3,17),(4,16)], 5: [(5,17),(3,11),(6,16),(3,19),(4,18)]}
        self.transition_dict[(2, 14)] = {1: [(1,14)], 3: [(2,14)], 5: [(2,14)], ORANGE: [(1,15)]}
        self.transition_dict[(2, 13)] = {1: [(2,14)], 3: [(1,15)], 5: [(2,13)], ORANGE: [(1,15)], PAY: 50}
        self.transition_dict[(2, 12)] = {1: [(1,12)], 3: [(2,13)], 5: [(1,14)]}
        self.transition_dict[(2, 11)] = {1: [(1,11),(3,11)], 3: [(5,11),(3,13),(3,9),(1,13)], 5: [(2,14),(3,15),(7,11),(5,13), (3,7), (2,8), (4,8)]}
        self.transition_dict[(2, 8)] = {1: [(1,8),(3,8)], 3: [(0,9),(3,10),(5,8),(3,6),(4,7)], 5: [(2,11),(1,11),(4,11),(3,12),(7,8),(4,5),(3,4)]}
        self.transition_dict[(2, 4)] = {1: [(1,4),(3,4)], 3: [(5,4),(3,6)], 5: [(7,4),(3,8)]}


    def init_row1(self):
        self.transition_dict[(1, 25)] = {1: [(0,25),(2,25)], 3: [(0,27),(0,23),(4,25),(3,26)], 5: [(0,21),(6,25)], ORANGE: True}
        self.transition_dict[(1, 20)] = {1: [(0,20),(2,20)], 3: [(0,22),(3,19),(4,20)], 5: [(0,24),(6,20),(4,18),(3,17)]}
        self.transition_dict[(1, 15)] = {1: [(2,15)], 3: [(3,16),(3,14)], 5: [(3,18),(5,16),(3,12)], PAY: 50, HAS: Certificate.TAX}
        self.transition_dict[(1, 14)] = {1: [(1,15)], 3: [(1,14)], 5: [(1,14)], ORANGE: True, WAIT: True}
        self.transition_dict[(1, 13)] = {1: [(0,13)], 3: [(0,13)], 5: [(0,13)]}
        self.transition_dict[(0, 13)] = {1: [(2,13)], 3: [(1,14)], 5: [(0,13)], ORANGE: True}
        self.transition_dict[(1, 12)] = {1: [(0,12)], 3: [(0,12)], 5: [(0,12)], PAY: 50}
        self.transition_dict[(0, 12)] = {1: [(1,13)], 3: [(2,14)], 5: [(1,15)]}
        self.transition_dict[(1, 11)] = {1: [(0,11),(2,11)], 3: [(1,12),(3,12),(3,10),(4,11)], 5: [(2,13),(5,12),(6,11),(3,14),(3,8),(4,9)]}
        self.transition_dict[(1, 8)] = {1: [(0,8),(2,8)], 3: [(0,11),(3,9),(3,7),(4,8)], 5: [(2,11),(3,11),(6,8),(3,5),(4,6)]}
        self.transition_dict[(1, 4)] = {1: [(0,4),(2,4),(1,0)], 3: [(3,5),(4,4)], 5: [(6,4),(3,7)]}
        # starting point
        self.transition_dict[(1, 0)] = {1: [(1,4)], 3: [(3,4)], 5: [(3,6),(5,4)]}


    def init_row0(self):
        self.transition_dict[(0, 27)] = {1: [(0,26)], 3: [(1,25),(0,24)], 5: [(2,26),(3,25),(0,22)]}
        self.transition_dict[(0, 26)] = {1: [(0,27),(0,25)], 3: [(2,25),(0,23)], 5: [(3,26),(4,25),(0,21)]}
        self.transition_dict[(0, 25)] = {1: [(0,26),(1,25),(0,24)], 3: [(2,26),(3,25),(0,22)], 5: [(5,25),(0,20)], ORANGE: True}
        self.transition_dict[(0, 24)] = {1: [(0,25),(0,23)], 3: [(2,25),(0,27),(0,21)], 5: [(3,26),(4,25),(1,20)]}
        self.transition_dict[(0, 23)] = {1: [(0,24),(0,22)], 3: [(1,25),(0,26),(0,20)], 5: [(2,26),(3,25),(2,20)]}
        self.transition_dict[(0, 22)] = {1: [(0,23),(0,21)], 3: [(0,25),(1,20)], 5: [(2,25),(0,27),(3,20)]}
        self.transition_dict[(0, 21)] = {1: [(0,22),(0,20)], 3: [(0,24),(2,20)], 5: [(1,25),(0,26),(4,20),(3,19)]}
        self.transition_dict[(0, 20)] = {1: [(0,21),(1,20)], 3: [(0,23),(3,20)], 5: [(0,25),(5,20),(3,18)]}
        self.transition_dict[(0, 11)] = {1: [(1,11)], 3: [(3,11),(2,12)], 5: [(1,13),(3,13),(5,11),(3,9)]}
        self.transition_dict[(0, 8)] = {1: [(0,9), (1,8)], 3: [(1,11), (3,8)], 5: [(3,11), (2,12), (5,8), (3,6), (3,10)]}
        self.transition_dict[(0, 9)] = {1: [(0,11)], 3: [(2,11)], 5: [(1,12),(3,12),(4,11),(3,10)], HAS: Certificate.GRANDMA}
        self.transition_dict[(0, 4)] = {1: [(1,4)], 3: [(3,4)], 5: [(3,6),(5,4)]}

